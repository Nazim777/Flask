from flask import Blueprint, request, render_template, redirect
from app.models.user import User as UserModel
from app.extension import db

bp = Blueprint("user",__name__)

@bp.route("/", methods=["GET","POST"])
def user():
    if request.method =="POST":
        new_user = UserModel(name=request.form['name'],email=request.form['email'])
        db.session.add(new_user)
        db.session.commit()
        return redirect("/")
    else:
      users = UserModel.query.all()
      print(users)
      return render_template("user/index.html",users=users)
    

@bp.route('/user/<int:id>',)
def single_user(id):
        user = UserModel.query.filter_by(id=id).first()
        return render_template("user/singleUser.html",user=user)
    

@bp.route("/user/delete/<int:id>")
def delete_user(id):
    user = UserModel.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect("/")



@bp.route('/user/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    print("user_id",id)
    if request.method=='POST':
        name = request.form["name"]
        email = request.form["email"]
        user = UserModel.query.filter_by(id=id).first()
        user.name = name
        user.email = email
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    else:
         user = UserModel.query.filter_by(id=id).first()
         return render_template('user/update.html', user=user)
    
   
        
   

    

