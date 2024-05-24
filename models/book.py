from app import mongo
class Book:
    def __init__(self, title, author, isbn, cover_image, description, publisher, published_date, genre, pages):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.cover_image = cover_image
        self.description = description
        self.publisher = publisher
        self.published_date = published_date
        self.genre = genre
        self.pages = pages
    
    def save(self):
        mongo.db.books.insert_one({
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'cover_image': self.cover_image
            'description': self.description,
            'publisher': self.publisher,
            'published_date': self.published_date,
            'genre': self.genre,
            'pages': self.pages
        })

    @staticmethod
    def get_all():
        return mongo.db.books.find({}, {'_id': False})

