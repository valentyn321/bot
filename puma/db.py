import sqlite3


def init_db(force: bool = False):
    conn = sqlite3.connect('puma_shoes.db')
    c = conn.cursor()

    if force:
        c.execute('DROP TABLE IF EXISTS sales')

    c.execute('''
        CREATE TABLE IF NOT EXISTS sales(
            id              INTEGER PRIMARY KEY,
            title           TEXT NOT NULL,
            link            TEXT NOT NULL,
            price_usd       REAL NOT NULL
        )
    ''')

    conn.commit()

def add_item(title: str, link: str, price_usd: float):
    conn = sqlite3.connect('puma_shoes.db')
    c = conn.cursor()
    c.execute('INSERT INTO sales (title, link, price_usd) VALUES (?, ?, ?)', (title, link, price_usd))
    conn.commit()
