import sqlite3

class Borrowing:
    def __init__(self, id, book_id, member_id):
        self.id = id
        self.book_id = book_id
        self.member_id = member_id
        
    @classmethod
    def create_table(cls):
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS borrowings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id INTEGER,
                member_id INTEGER,
                FOREIGN KEY (book_id) REFERENCES books (id),
                FOREIGN KEY (member_id) REFERENCES members (id)
            )
        ''')
        conn.commit()
        conn.close()
        
    def save(self):
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("INSERT INTO borrowings (book_id, member_id) VALUES (?, ?)",
                           (self.book_id, self.member_id))
            self.id = cursor.lastrowid
            # Update book status to borrowed
            cursor.execute("UPDATE books SET is_borrowed=1 WHERE id=?", (self.book_id,))
        conn.commit()
        conn.close()
        
    @classmethod
    def return_book(cls, book_id):
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        # Delete the borrowing record and mark the book as available
        cursor.execute("DELETE FROM borrowings WHERE book_id=?", (book_id,))
        cursor.execute("UPDATE books SET is_borrowed=0 WHERE id=?", (book_id,))
        conn.commit()
        conn.close()
