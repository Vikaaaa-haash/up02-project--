"""Модели данных для проекта УП.02."""


class Product:
    """Класс Товар (Автомобиль)."""

    def __init__(self, product_id, marka, model, year, price, quantity, photo=""):
        """
        Инициализация автомобиля.

        :param product_id: идентификатор
        :param marka: марка
        :param model: модель
        :param year: год выпуска
        :param price: цена
        :param quantity: количество на складе
        :param photo: имя файла фото
        """
        self.id = product_id
        self.marka = marka
        self.model = model
        self.year = year
        self.price = price
        self.quantity = quantity
        self.photo = photo

    def full_name(self):
        """Полное имя: «Марка Модель (год)»."""
        return f"{self.marka} {self.model} ({self.year})"

    def total(self):
        """Общая стоимость (цена × количество)."""
        return self.price * self.quantity

    def price_with_discount(self, discount_percent):
        """Цена со скидкой."""
        return self.price * (1 - discount_percent / 100)

    def indicator(self):
        """Индикатор «много/мало» (порог 5)."""
        return "много" if self.quantity > 5 else "мало"

    def is_low_stock(self):
        """True, если количество ≤ 3."""
        return self.quantity <= 3

    def info(self):
        """Строка с информацией об автомобиле."""
        return (
            f"{self.full_name()}: "
            f"{int(self.price)} руб. × {self.quantity} = {int(self.total())} руб. "
            f"({self.indicator()})"
        )