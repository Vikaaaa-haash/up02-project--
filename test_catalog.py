"""Тестирование каталога (вариант 11 — Автомобили)."""
import database as db


def test_db_available():
    """Проверяет, что БД доступна."""
    try:
        products = db.get_all_products()
        return isinstance(products, list)
    except Exception as e:
        print(f"❌ БД недоступна: {e}")
        return False


def test_products_count():
    """Проверяет, что товары загружены."""
    products = db.get_all_products()
    return len(products) > 0


def test_product_fields():
    """Проверяет, что у всех товаров достаточно полей."""
    products = db.get_all_products()
    for p in products:
        if len(p) < 7:                          # у вас 7 полей
            print(f"❌ Товар id={p[0]}: мало полей ({len(p)})")
            return False
    return True


def test_prices_are_numbers():
    """Проверяет, что все цены — числа."""
    products = db.get_all_products()
    for p in products:
        if not isinstance(p[4], (int, float)):   # цена — p[4]
            print(f"❌ Товар id={p[0]}: цена не число")
            return False
    return True


def test_quantity_not_negative():
    """Проверяет, что количество не отрицательное."""
    products = db.get_all_products()
    for p in products:
        if p[5] is None or p[5] < 0:             # количество — p[5]
            print(f"❌ Товар id={p[0]}: отрицательное количество")
            return False
    return True


def test_names_not_empty():
    """Проверяет, что у всех товаров есть марка (не пустая)."""
    products = db.get_all_products()
    for p in products:
        if not p[1]:                             # марка — p[1]
            print(f"❌ Товар id={p[0]}: пустая марка")
            return False
    return True


def test_has_image():
    """Проверяет, что хотя бы у одного товара есть изображение (ДЗ)."""
    products = db.get_all_products()
    for p in products:
        if p[6]:                                 # фото — p[6]
            return True
    print("⚠️ Ни у одного товара нет изображения")
    return False


def run_all_tests():
    """Прогон всех тестов каталога."""
    tests = [
        ("БД доступна", test_db_available),
        ("Товары загружены", test_products_count),
        ("У всех товаров нужные поля", test_product_fields),
        ("Все цены — числа", test_prices_are_numbers),
        ("Количество не отрицательное", test_quantity_not_negative),
        ("Марки не пустые", test_names_not_empty),
        ("Хотя бы одно изображение", test_has_image),   # ← ДЗ
    ]

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ КАТАЛОГА")
    print("=" * 60)

    passed = 0
    for name, func in tests:
        result = func()
        status = "✅" if result else "❌"
        if result:
            passed += 1
        print(f"{status} {name}")

    print("=" * 60)
    print(f"Пройдено: {passed} / {len(tests)}")


if __name__ == "__main__":
    run_all_tests()