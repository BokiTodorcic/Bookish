from flask import request
from bookish.models.book import Book
from bookish.models.bookCopy import BookCopy
from bookish.models.user import User
from bookish.models import db


def bookish_routes(app):   
    @app.route('/healthcheck')
    def health_check():
        return {"status": "OK"}

    @app.route('/user', methods=['POST', 'GET'])
    def handle_user():
        if request.method == 'POST':
            if request.is_json:
                data = request.get_json()
                new_user = User(first_name=data['first_name'], last_name=data['last_name'])
                db.session.add(new_user)
                db.session.commit()
                return {"message": "New user has been created successfully."}
            else:
                return {"error": "The request payload is not in JSON format"}

        elif request.method == 'GET':
            users = User.query.all()
            results = [
                {
                    'id': users.id,
                    'first_name': users.first_name,
                    'last_name': users.last_name
                } for users in users]
            return {"Users": results}
        
    @app.route('/books', methods=['POST', 'GET'])
    def handle_books():
        if request.method == 'POST':
            if request.is_json:
                data = request.get_json()
                new_book = Book(title=data['title'], author=data['author'])
                db.session.add(new_book)
                db.session.commit()
                return {"message": "New book has been added successfully."}
            else:
                return {"error": "The request payload is not in JSON format"}

        elif request.method == 'GET':
            # books = Book.query.all()
            books = db.session.execute(db.select(Book)).all()
            print(books)
            results = [
                {
                    'ISBN': books.ISBN,
                    'title': books.title,
                    'author': books.author
                } for book in books]
            return {"Books": books}
