from sqlalchemy.orm import Mapped, mapped_column
from app.extension import db

class User(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String, nullable=False)
    email: Mapped[str] = mapped_column(db.String,unique=True, nullable=False)

