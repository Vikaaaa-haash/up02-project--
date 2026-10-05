"""Проверка класса Product."""
from models import Product


# Создаём один автомобиль вручную
p = Product(
    product_id=1,
    marka="Toyota",
    model="Camry",
    year=2020,
    price=2500000,
    quantity=3,
    photo="camry.png"
)

print(p.info())
print(f"Со скидкой 25%: {p.price_with_discount(25):.0f} руб.")
print(f"Полное имя: {p.full_name()}")
print(f"Низкий остаток? {p.is_low_stock()}")