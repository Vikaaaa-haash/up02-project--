"""Загрузка заказов из БД в объекты класса Order."""
import sqlite3
from config import DB_PATH
from models import Product, Order


def _row_to_product(row):
    """Строка БД → объект Product."""
    return Product(
        product_id=row[0],
        marka=row[1],
        model=row[2],
        year=row[3],
        price=row[4],
        quantity=row[5],
        photo=row[6]
    )


def get_product_by_id(product_id):
    """Возвращает объект Product по его id."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Товар WHERE id = ?", (product_id,))
    row = cur.fetchone()
    conn.close()
    return _row_to_product(row) if row else None


def get_all_orders():
    """Возвращает список объектов Order из БД."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Заказ ORDER BY id")
    rows = cur.fetchall()
    conn.close()

    orders = []
    for row in rows:
        # row[0]=id, row[1]=дата, row[2]=клиент, row[3]=товар_id, row[4]=количество
        product = get_product_by_id(row[3])
        order = Order(
            order_id=row[0],
            date=row[1],
            client=row[2],
            product=product,
            quantity=row[4]
        )
        orders.append(order)
    return orders


def print_orders(orders):
    """Выводит информацию о заказах."""
    print(f"\n{'=' * 70}")
    print(f"ВСЕГО ЗАКАЗОВ: {len(orders)}")
    print("=" * 70)
    for o in orders:
        print(o.info())
        print("-" * 70)


if __name__ == "__main__":
    orders = get_all_orders()
    print_orders(orders)