"""Загрузка автомобилей из БД в объекты класса Product."""
import sqlite3
from config import DB_PATH
from models import Product


def _row_to_product(row):
    """Преобразует строку из БД в объект Product (вариант 11)."""
    return Product(
        product_id=row[0],
        marka=row[1],
        model=row[2],
        year=row[3],
        price=row[4],
        quantity=row[5],
        photo=row[6]
    )


def get_all_products():
    """Все автомобили."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Товар ORDER BY id")
    rows = cur.fetchall()
    conn.close()
    return [_row_to_product(r) for r in rows]


def get_products_by_marka(marka):
    """Автомобили одной марки (аналог «категории»)."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Товар WHERE марка = ?", (marka,))
    rows = cur.fetchall()
    conn.close()
    return [_row_to_product(r) for r in rows]


def get_products_low_stock():
    """Автомобили с количеством ≤ 3."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Товар WHERE количество <= 3")
    rows = cur.fetchall()
    conn.close()
    return [_row_to_product(r) for r in rows]


def print_catalog_with_highlight(products):
    """Выводит каталог с подсветкой для товаров ≤3."""
    print(f"\n{'=' * 70}")
    print(f"КАТАЛОГ ({len(products)} шт.)")
    print("=" * 70)

    for p in products:
        # :<3 — фиксированная ширина, чтобы ⚠️ не «съедал» пробел
        highlight = "⚠️" if p.is_low_stock() else "  "
        print(f"{highlight:<3} {p.info()}")

    print("=" * 70)


if __name__ == "__main__":
    print("1. Все автомобили:")
    print_catalog_with_highlight(get_all_products())

    print("\n2. Автомобили марки Toyota:")
    print_catalog_with_highlight(get_products_by_marka("Toyota"))

    print("\n3. Автомобили с низким остатком (≤3):")
    print_catalog_with_highlight(get_products_low_stock())