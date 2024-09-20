import sqlite3

class Member:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name
        
    @classmethod
    def create_table(cls):
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS members (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
        
    def save(self):
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute('''
                INSERT INTO members (name)
                VALUES (?)
            ''', (self.name,))
            self.id = cursor.lastrowid
        else:
            cursor.execute('''
                UPDATE members
                SET name = ?
                WHERE id = ?
            ''', (self.name, self.id))
        conn.commit()
        conn.close()
        
    @classmethod
    def fetch_all(cls):
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM members")
        member_data = cursor.fetchall()
        conn.close()
        return [cls(id=member[0], name=member[1]) for member in member_data]
    
    @classmethod
    def find_by_id(cls, member_id):
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM members WHERE id = ?",
            (member_id,))
        member = cursor.fetchone()
        conn.close()
        if member:
            return cls(id=member[0], name=member[1])
        else:
            return None
        
    @classmethod
    def update(cls, member_id, new_name):
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE members SET name=? WHERE id=?",
        (new_name, member_id))
        conn.commit()
        conn.close()
        
    @classmethod
    def delete(cls, member_id):
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM members WHERE id=?",
        (member_id,))
        conn.commit()
        conn.close()
