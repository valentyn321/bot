import sqlite3


def init_db(name_of_table: str, force: bool = False):
    conn = sqlite3.connect(name_of_table)
    c = conn.cursor()

    if force:
        c.execute('DROP TABLE IF EXISTS sales')

    c.execute('''
        CREATE TABLE IF NOT EXISTS sales(
            id              INTEGER PRIMARY KEY,
            title           TEXT NOT NULL,
            link            TEXT NOT NULL,
            price_uah       REAL NOT NULL
        )
    ''')

    conn.commit()

def add_item(title: str, link: str, price_uah: float, name_of_table):
    conn = sqlite3.connect(name_of_table)
    c = conn.cursor()
    c.execute('INSERT INTO sales (title, link, price_uah) VALUES (?, ?, ?)', (title, link, price_uah))
    conn.commit()