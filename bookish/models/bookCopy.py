from bookish.app import db

class BookCopy(db.Model):
    __tablename__ = 'copies_table'

    ISBN = db.Column(db.Integer, db.ForeignKey("books_table.ISBN"), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users_table.id"))
    due_date = db.Column(db.Date)

    def __init__(self, user_id, due_date):
        self.user_id = user_id
        self.due_date = due_date

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'ISBN': self.ISBN,
            'user_id': self.user_id,
            'due_date': self.due_date
        }
