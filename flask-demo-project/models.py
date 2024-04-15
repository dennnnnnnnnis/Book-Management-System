from extension import db

class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_number = db.Column(db.String(255), nullable=False)
    book_name = db.Column(db.String(255), nullable=False)
    book_type = db.Column(db.String(255), nullable=False)
    book_price = db.Column(db.Float, nullable=False)
    author = db.Column(db.String(255))
    book_publisher = db.Column(db.String(255))

    @staticmethod
    def init_db():
        books = [
            (1, '001', 'book1', 'action', 40, 'author1', 'publisher1'),
            (2, '002', 'book2', 'fiction', 50, 'author2', 'publisher2')
        ]
        for entry in books:
            book = Book()
            book.id = entry[0]
            book.book_number = entry[1]
            book.book_name = entry[2]
            book.book_type = entry[3]
            book.book_price = entry[4]
            book.author = entry[5]
            book.book_publisher = entry[6]
            db.session.add(book)
        db.session.commit()