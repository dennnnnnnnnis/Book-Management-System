#导入flask对象
from flask import Flask, request
from flask.views import MethodView
from extension import db, cors
from models import Book

# 用flask对象创建一个app对象
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///demo_project.sqlite"
app.config['SQLALCHEMY_TRACK_MODEFICATIONS'] = False
db.init_app(app)
cors.init_app(app)

#路由
@app.route('/') # 访问的路径
def hello():
    return 'Hello, World!'

@app.cli.command()
def create():
    db.drop_all()
    db.create_all()
    Book.init_db()

class BookApi(MethodView):
    def get(self, book_id):
        # If not get the detail of a single book, get all the books
        if not book_id:
            books: [Book] = Book.query.all()
            results = [
                {
                    "id": book.id,
                    "book_name": book.book_name,
                    "book_type": book.book_type,
                    "book_price": book.book_price,
                    "book_number": book.book_number,
                    "book_publisher": book.book_publisher,
                    "author": book.author
                } for book in books
            ]
            return {
                'status': 'success',
                'message': 'Data successfully retrived',
                'results': results
            }
        # else only want the specifc book info
        book: Book = Book.query.get(book_id)
        return {
            'status': 'success',
            'message': 'Data successfully retrived',
            'results': {
                "id": book.id,
                "book_name": book.book_name,
                "book_type": book.book_type,
                "book_price": book.book_price,
                "book_number": book.book_number,
                "book_publisher": book.book_publisher,
                "author": book.author
            }
        }
    
    # add new book
    def post(self):
        form = request.json # from user input
        book = Book()
        book.book_number = form.get("book_number")
        book.book_name = form.get("book_name")
        book.book_type = form.get("book_type")
        book.book_price = form.get("book_price")
        book.author = form.get("author")
        book.book_publisher = form.get("book_publisher")
        db.session.add(book)
        db.session.commit()
        return {
            "status": "success",
            "message": "Book successfully added"
        }
    
    def delete(self, book_id):
        book = Book.query.get(book_id)
        db.session.delete(book)
        db.session.commit()
        return {
            "status": "success",
            "message": "Book successfully deleted"
        }
    
    # edit the book info
    def put(self, book_id):
        form = request.json # from user input
        book: Book = Book.query.get(book_id)
        book.book_number = form.get("book_number")
        book.book_name = form.get("book_name")
        book.book_type = form.get("book_type")
        book.book_price = form.get("book_price")
        book.author = form.get("author")
        book.book_publisher = form.get("book_publisher")
        db.session.commit()
        return {
            "status": "success",
            "message": "Book info successfully changed"
        }

book_view = BookApi.as_view('book_api')
app.add_url_rule('/books/', defaults={'book_id': None}, 
                 view_func=book_view, methods=['GET'])
app.add_url_rule('/books/addBook', view_func=book_view, methods=['POST'])
app.add_url_rule('/books/<int:book_id>', view_func=book_view, 
                 methods=['GET', 'PUT', 'DELETE'])
