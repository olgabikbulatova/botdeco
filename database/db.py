import sqlite3 as sq


db = sq.connect('database/my_db.db')
cur = db.cursor()


async def db_start():
    cur.execute('''CREATE TABLE IF NOT EXISTS orders(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id INTEGER,
                name TEXT,
                phone,
                description TEXT)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS application(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id,
                name TEXT,
                phone,
                kitchen_type,
                kitchen_material,
                order_date)''')
    db.commit()


def find_order(order_id):
    cur.execute("SELECT * FROM orders WHERE order_id=?", (order_id,))
    results = cur.fetchall()
    text_for_admin = ''
    for row in results:
        for col in row:
            text_for_admin += f' {str(col)}'
    return text_for_admin


def insert_db(user_id, name, phone, kitchen_type, kitchen_material, order_date):
    sqlite_insert_data = """INSERT INTO application
                              (user_id, name, phone, kitchen_type, kitchen_material, order_date) 
                              VALUES (?, ?, ?, ?, ?,?)"""
    cur.execute(sqlite_insert_data, (user_id, name, phone, kitchen_type, kitchen_material, order_date))
    db.commit()


# def find_order(user_id):
#     cur.execute("SELECT * FROM application WHERE user_id=?", (user_id,))
#     results = cur.fetchall()
#     text_for_admin = ''
#     for row in results:
#         for col in row:
#             text_for_admin += f' {str(col)}'
#     return text_for_admin






