"""Загрузка автомобилей из БД с расширенным выводом."""
import sqlite3
from config import DB_PATH


def get_all_products():
    """Все автомобили."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Товар ORDER BY id")
    products = cur.fetchall()
    conn.close()
    return products


def get_products_by_marka(marka):
    """Автомобили одной марки (аналог «категории»)."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Товар WHERE марка = ?", (marka,))
    products = cur.fetchall()
    conn.close()
    return products


def get_products_low_stock():
    """Автомобили с количеством ≤ 3."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Товар WHERE количество <= 3")
    products = cur.fetchall()
    conn.close()
    return products


def get_marks():
    """Список всех марок."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT марка FROM Товар ORDER BY марка")
    marks = [row[0] for row in cur.fetchall()]
    conn.close()
    return marks


def print_catalog(products):
    """Каталог с индикатором много/мало и подсветкой."""
    print(f"\n{'=' * 60}")
    print(f"КАТАЛОГ АВТОМОБИЛЕЙ ({len(products)} шт.)")
    print("=" * 60)

    for p in products:
        # Распаковка для варианта 11
        car_id, marka, model, year, price, qty, photo = p

        indicator = "много" if qty > 5 else "мало"
        highlight = "⚠️  " if qty <= 3 else "  "

        print(f"{highlight} {car_id}. {marka} {model} ({year})")
        print(f"    Цена: {int(price)} руб. | Кол-во: {qty} ({indicator})")

    print("=" * 60)


if __name__ == "__main__":
    print("1. Все автомобили:")
    print_catalog(get_all_products())

    print("\n2. Марки автомобилей в базе:")
    for marka in get_marks():
        print(f"   - {marka}")

    print("\n3. Автомобили с низким остатком (≤3):")
    print_catalog(get_products_low_stock())