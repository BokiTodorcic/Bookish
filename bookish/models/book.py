from bookish.app import db

class Book(db.Model):
    __tablename__ = 'books_table'

    isbn = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return '<isbn {}>'.format(self.isbn)

    def serialize(self):
        return {
            'isbn': self.isbn,
            'title': self.title,
            'author': self.author
        }
