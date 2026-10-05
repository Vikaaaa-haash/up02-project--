from datetime import datetime
from models import Product

# Audi A6 (id=4) — нет заказов в сентябре → скидка 25%
p = Product(
    product_id=4,
    marka="Audi",
    model="A6",
    year=2022,
    price=5000000,
    quantity=2,
    photo=""
)

date = datetime(2026, 10, 15)
print(f"Базовая цена: {int(p.price)}")
print(f"Со скидкой: {int(p.price_with_discount_auto(date))}")

# Toyota Camry (id=1) — ЕСТЬ заказ в сентябре → без скидки
p2 = Product(1, "Toyota", "Camry", 2020, 2500000, 3, "")
print(f"\nToyota Camry (есть заказ):")
print(f"Базовая цена: {int(p2.price)}")
print(f"Со скидкой: {int(p2.price_with_discount_auto(date))}")