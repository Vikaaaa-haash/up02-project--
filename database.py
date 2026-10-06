"""Работа с базой данных."""
import sqlite3
from config import DB_PATH


def get_all_products():
    """Возвращает список всех автомобилей (кортежи)."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Товар ORDER BY id")
    rows = cur.fetchall()
    conn.close()
    return rows
def get_all_marks():
    """Возвращает список уникальных марок."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT марка FROM Товар ORDER BY марка")
    marks = [row[0] for row in cur.fetchall()]
    conn.close()
    return marks