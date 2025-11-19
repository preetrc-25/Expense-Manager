# db.py
import sqlite3

DB = "expenses.db"

def conn():
    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row
    return c

def init_db():
    c = conn(); cur = c.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS categories(id INTEGER PRIMARY KEY, name TEXT UNIQUE)")
    cur.execute("""CREATE TABLE IF NOT EXISTS transactions(
                   id INTEGER PRIMARY KEY, date TEXT, desc TEXT, amount REAL, category TEXT, kind TEXT)""")
    c.commit(); c.close()

def add_category(name):
    c = conn(); cur = c.cursor()
    try:
        cur.execute("INSERT INTO categories(name) VALUES(?)", (name,))
        c.commit()
    except sqlite3.IntegrityError:
        pass
    c.close()

def get_categories():
    c = conn(); cur = c.cursor()
    cur.execute("SELECT name FROM categories ORDER BY name")
    rows = [r["name"] for r in cur.fetchall()]
    c.close(); return rows

def add_tx(date, desc, amount, category, kind):
    c = conn(); cur = c.cursor()
    cur.execute("INSERT INTO transactions(date, desc, amount, category, kind) VALUES(?,?,?,?,?)",
                (date, desc, amount, category, kind))
    c.commit(); c.close()

def get_txs():
    c = conn(); cur = c.cursor()
    cur.execute("SELECT id, date, desc, amount, category, kind FROM transactions ORDER BY id DESC")
    rows = [dict(r) for r in cur.fetchall()]
    c.close(); return rows

def delete_tx(txid):
    c = conn(); cur = c.cursor()
    cur.execute("DELETE FROM transactions WHERE id=?", (txid,))
    c.commit(); c.close()

# ensure DB ready when imported
init_db()
