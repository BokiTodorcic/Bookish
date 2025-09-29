from flask import request
from bookish.models.book import Book
from bookish.models.bookCopy import BookCopy
from bookish.models.user import User
from bookish.models import db


def bookish_routes(app):   
    @app.route('/healthcheck')
    def health_check():
        return {"status": "OK"}

    @app.route('/users', methods=['POST', 'GET'])
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
            users = db.session.execute(db.select(User)).scalars().all()
            results = [user.serialize() for user in users]
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
            books = db.session.execute(db.select(Book)).scalars().all()
            results = [book.serialize() for book in books]
            return {"Books": results}
        
    @app.route('/bookcopies', methods=['POST', 'GET'])
    def handle_bookcopies():
        if request.method == 'POST':
            if request.is_json:
                data = request.get_json()
                new_copy = BookCopy(isbn=data['isbn'], user_id=data.get('user_id'), due_date=data.get('due_date'))
                db.session.add(new_copy)
                db.session.commit()
                return {"message": "New book copy has been added successfully."}
            else:
                return {"error": "The request payload is not in JSON format"}

        elif request.method == 'GET':
            copies = db.session.execute(db.select(BookCopy)).scalars().all()
            results = [copy.serialize() for copy in copies]
            return {"Copies": results}

