"""Проверка вывода полей."""
import database as db


def test_fields():
    """Проверяет, что все поля на месте."""
    products = db.get_all_products()
    print(f"Всего автомобилей: {len(products)}")

    required_count = 7   # у нас 7 полей: id, марка, модель, год, цена, кол-во, фото
    errors = 0

    for p in products:
        if len(p) < required_count:
            print(f"❌ Товар id={p[0]}: мало полей ({len(p)})")
            errors += 1

    if errors == 0:
        print(f"✅ Все {len(products)} товаров содержат нужные поля")
    else:
        print(f"❌ Найдено ошибок: {errors}")


def test_prices():
    """Проверяет, что у всех товаров есть цена."""
    products = db.get_all_products()
    for p in products:
        if p[4] is None:              # цена — product[4]
            print(f"❌ Товар id={p[0]}: нет цены")
            return
    print("✅ У всех товаров есть цена")


def test_quantities():
    """Проверяет, что количество ≥ 0."""
    products = db.get_all_products()
    for p in products:
        if p[5] is None or p[5] < 0:   # количество — product[5]
            print(f"❌ Товар id={p[0]}: некорректное количество")
            return
    print("✅ У всех товаров количество ≥ 0")


def test_has_image():
    """Проверяет, что хотя бы у одного товара есть изображение."""
    products = db.get_all_products()
    for p in products:
        if p[6]:                       # фото — product[6]
            print(f"✅ Есть товар с изображением: {p[1]} {p[2]}")
            return
    print("⚠️ Ни у одного товара нет изображения")


if __name__ == "__main__":
    test_fields()
    test_prices()
    test_quantities()
    test_has_image()