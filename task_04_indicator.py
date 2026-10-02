# task_04_indicator.py

catalog = [
    {"name": "Кроссовки", "price": 8500, "qty": 3},
    {"name": "Ботинки", "price": 15000, "qty": 1},
    {"name": "Туфли", "price": 12000, "qty": 5},
    {"name": "Сандалии", "price": 4500, "qty": 8},
    {"name": "Кеды", "price": 6000, "qty": 2},
]

sorted_catalog = sorted(catalog, key=lambda item: item["qty"] > 5, reverse=True)

print("Каталог с индикатором:")

for i, item in enumerate(sorted_catalog, start=1):
    indicator = "много" if item["qty"] > 5 else "мало"
    print(f"{i}. {item['name']} — {item['qty']} шт. → {indicator}")