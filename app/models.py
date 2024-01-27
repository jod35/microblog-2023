import sqlalchemy.orm as so
import sqlalchemy as sa
from app import db
from datetime import datetime
from typing import List


class User(db.Model):
    __tablename__ = "users"
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(250), nullable=False)
    email: so.Mapped[str] = so.mapped_column(
        sa.String(120), nullable=False, unique=True
    )
    password_hash: so.Mapped[str] = so.mapped_column(nullable=True)
    posts :so.Mapped[List["Post"]] = so.relationship(backref="author")

    def __repr__(self) -> str:
        return f"<User {self.username}>"


class Post(db.Model):
    __tablename__ = "posts"
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(nullable=False)
    body: so.Mapped[str] = so.mapped_column(sa.Text(), nullable=False)
    created_at: so.Mapped[datetime] = so.mapped_column(
        sa.DateTime, default=datetime.utcnow
    )
    user_id: so.Mapped[int] = so.mapped_column(
        sa.Integer(), sa.ForeignKey("users.id"), nullable=False, index=True
    )

    author: so.Mapped["User"] = so.relationship("User", backref="posts")

    def __repr__(self):
        return f"<User {self.title}>"