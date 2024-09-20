import sqlite3

class Book:
    def __init__(self, id, title, author, is_borrowed=False):
        self.id = id
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        
    @classmethod
    def create_table(cls):
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                is_borrowed INTEGER NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
        
    def save(self):
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("INSERT INTO books (title, author, is_borrowed) VALUES (?, ?, ?)",
                           (self.title, self.author, self.is_borrowed))
            self.id = cursor.lastrowid
        else:
            cursor.execute("UPDATE books SET title=?, author=?, is_borrowed=? WHERE id=?",
                           (self.title, self.author, self.is_borrowed, self.id))
        conn.commit()
        conn.close()
        
    @classmethod
    def fetch_all(cls):
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        book_data = cursor.fetchall()
        conn.close()
        return [cls(id=book[0], title=book[1], author=book[2], is_borrowed=book[3]) for book in book_data]
    
    @classmethod
    def find_by_id(cls, book_id):
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE id =?",
                       (book_id,))
        book = cursor.fetchone()
        conn.close()
        if book:
            return cls(id=book[0], title=book[1], author=book[2], is_borrowed=book[3])
        else:
            return None
    
    @classmethod
    def delete(cls, book_id):
        conn = sqlite3.connect("library.db")
        cursor= conn.cursor()
        cursor.execute("DELETE FROM books WHERE id =?",
                       (book_id,))
        conn.commit()
        conn.close()
