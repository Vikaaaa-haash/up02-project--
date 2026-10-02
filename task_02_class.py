# task_02_class.py

class Product:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    def total(self):
        """Общая стоимость: цена × количество."""
        return self.price * self.qty

    def info(self):
        """Строка с информацией о товаре."""
        return f"{self.name}: {self.price} × {self.qty} = {self.total()} руб."


# Создаём 3 объекта
p1 = Product("Кроссовки", 8500, 3)
p2 = Product("Ботинки", 15000, 1)
p3 = Product("Туфли", 12000, 5)

# Выводим информацию о каждом
print(p1.info())
print(p2.info())
print(p3.info())