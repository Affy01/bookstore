import sqlite3


class sql_db:
    """
    Class for db communication
    """

    def __init__(self, db_name):
        """
        init method
        :param db_name: Db to connect to
        :returns: cursor pointing to the db
        """
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book \
            (id INTEGER PRIMARY KEY, \
            title text, \
            author text, \
            year integer, \
            isbn integer)")
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        """
        Inserts a new row in the db
        :param title: Name of the book
        :param author: Name of the author
        :param year: Year published
        :param isbn: isbn code
        """
        self.cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        self.conn.commit()

    def get_all(self):
        """
        Gets all entries from the db
        """
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        print(rows)
        # if rows(1) == "CloudAtlas":
        #     rows(1) = "testBook"
        return rows

    def search(self, title="", author="", year="", isbn=""):
        """
        Looks for an entry in the db
        """
        self.cur.execute("SELECT * from book WHERE title=? OR author=? OR year =? OR isbn=?",
                         (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        """
        Deletes an entry
        """
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, title="", author="", year="", isbn=""):
        """
        Updates existing entry in the db
        """
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",
                         (title, author, year, isbn, id))
        self.conn.commit()

