from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String, nullable=True)
    book_name = db.Column(db.String, nullable=True)
    publisher = db.Column(db.DateTime, nullable=False, default=func.now())
    id_read = db.Column(db.Boolean, nullable=False, default=False)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id", ondelete='SET NULL'))
    genre = relationship("Genre", back_populates="books")

    def __repr__(self):
        return f"User(fullname={self.author_name!r})"


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String)
    books = relationship(
        "Book", back_populates="genre"
    )


