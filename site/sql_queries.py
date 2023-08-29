import sqlite3

conn = sqlite3.connect("Artistc.db") # з'єднання з базою даних (БД)
cursor = conn.cursor() #курсор (посилання) на БД

class ShopDB:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.db_name = "shop.db"
    def open(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
    def close(self):
        self.cursor.close()
        self.conn.close()
    
    def get_all_items(self):
        self.open()
        self.cursor.execute("SELECT * FROM items")
        data=self.cursor.fetchall()
        self.close()
        return data
    
    def get_item(self, id):
        self.open()
        self.cursor.execute("SELECT * FROM items WHERE id==(?)",[id])
        data=self.cursor.fetchone()
        self.close()
        return data