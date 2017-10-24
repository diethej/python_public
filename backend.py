import sqlite3
import csv
import pandas as pd



class Database:

    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM books")
        rows=self.cur.fetchall()
        return rows

    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows=self.cur.fetchall()
        return rows

    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()

    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
        self.conn.commit()


    def delete(self,id):
        self.cur.execute("DELETE FROM books WHERE id=?",(id,))
        self.conn.commit()


    def download(self):
        with open('test.txt','w') as write_file:
            self.conn = sqlite3.connect('books_database.db')
            self.cur = self.conn.cursor()
            for row in self.cur.execute("SELECT * FROM books"):
                rows= str(self.cur.fetchall())
                writer = csv.writer(write_file)
                write_file.write(rows)
                write_file.close()
            self.conn.commit()



    def __del__(self):
        self.conn.close()
