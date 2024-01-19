#!/usr/bin/env python

import os
import pandas as pd
from flask import Flask, request
from flask import render_template

from database import db, Book, Genre

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)


with app.app_context():
    db.drop_all()
    db.create_all()
    df = pd.read_csv("books.csv",
                     delimiter=";",
                     names=['Автор', 'Название', 'Жанр'],
                     index_col=None)
    genre_df = df['Жанр'].unique()
    for genre in genre_df :
        genre_name = Genre(genre_name=genre)
        db.session.add(genre_name)
    resources = Genre.query.all()
    for item in df.iterrows():
        for resource in resources:
            if resource.genre_name == item[1]['Жанр']:
                book = Book(author_name=item[1]['Автор'],
                            book_name=item[1]['Название'],
                            genre=resource)
                break
        db.session.add(book)
    db.session.commit()


@app.route("/",  methods=['GET', 'POST'])
def all_book():

    if request.method == 'POST':
        if request.form.get('Прочитано'):
            book.id_read = True
            books = Book.query.all()
            return render_template("all_books.html", books=books)
    elif request.method == 'GET':
        books = Book.query.all()
        return render_template("all_books.html", books=books)
#
#
@app.route("/genre/")
def all_genre():
    genres = Genre.query.all()
    return render_template("all_genre.html", genres=genres)

@app.route("/genre/<int:genre_id>")
def books_by_genre(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    return render_template(
        "genre_by_book.html",
        genre_name=genre.genre_name,
        books=genre.books,
        )


if __name__ == '__main__':
    app.run()
