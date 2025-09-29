from bookish.app import db

class BookInstance(db.Model):
    __tablename__ = 'Book_instances'

    isbn = db.Column(db.Integer, db.ForeignKey("books_table.isbn"), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users_table.id"))
    due_date = db.Column(db.Date)

    def __init__(self, isbn, user_id, due_date):
        self.isbn = isbn
        self.user_id = user_id
        self.due_date = due_date

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'isbn': self.isbn,
            'user_id': self.user_id,
            'due_date': self.due_date
        }
