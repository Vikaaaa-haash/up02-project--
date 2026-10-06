"""Каталог автомобилей (вариант 11) — рефакторинг."""
import tkinter as tk

from styles import (
    COLOR_MAIN_BG, COLOR_HIGHLIGHT,
    FONT_SIZE_NORMAL, FONT_SIZE_HEADER, FONT_SIZE_TITLE,
    font,
)
from resources import get_product_image


def create_product_card(parent, product):
    """Создаёт карточку автомобиля по макету."""
    qty = product[5]                       # количество — product[5]
    bg_color = _get_card_color(qty)

    card = tk.Frame(parent, bg=bg_color, bd=1, relief="solid")
    card.pack(fill="x", padx=10, pady=5)

    _add_image(card, product, bg_color)
    _add_text_info(card, product, bg_color, qty)

    return card


def _get_card_color(qty):
    """Возвращает цвет фона карточки."""
    return COLOR_HIGHLIGHT if qty <= 3 else COLOR_MAIN_BG


def _add_image(card, product, bg_color):
    """Добавляет изображение автомобиля (или заглушку)."""
    img_frame = tk.Frame(card, bg=bg_color)
    img_frame.pack(side="left", padx=10, pady=10)

    photo = product[6]                     # фото — product[6]
    if photo:
        image_path = f"resources/{photo}"
    else:
        image_path = "resources/picture.png"

    img = get_product_image(image_path, size=(100, 100))
    if img:
        img_label = tk.Label(img_frame, image=img, bg=bg_color)
        img_label.image = img
        img_label.pack()
    else:
        tk.Label(img_frame, text="[НЕТ ФОТО]", bg=bg_color,
                 width=10, height=5).pack()


def _add_text_info(card, product, bg_color, qty):
    """Добавляет текстовую информацию об автомобиле."""
    text_frame = tk.Frame(card, bg=bg_color)
    text_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    # Обработка крайних случаев (пустых полей)
    marka = product[1] if product[1] else "[Без марки]"
    model = product[2] if product[2] else "[Без модели]"
    year = product[3] if product[3] else "—"
    price = product[4] if product[4] is not None else 0

    _add_label(text_frame, f"{marka} | {model}",
               bg_color, bold=True, size=FONT_SIZE_TITLE)
    _add_label(text_frame, f"Год: {year}", bg_color)
    _add_label(text_frame, f"Количество: {_indicator(qty)} ({qty})", bg_color)
    _add_label(text_frame, f"{int(price)} руб.",
               bg_color, bold=True, size=FONT_SIZE_HEADER, align="e")
    # Товар с ценой > 1 000 000
    if price > 1000000:
        price_str = f"{int(price):,} руб.".replace(",", " ")
    else:
        price_str = f"{int(price)} руб."

    # Товар с очень длинным названием
    full_name = f"{marka} | {model}"
    if len(full_name) > 50:
        full_name = full_name[:47] + "..."

    _add_label(text_frame, full_name,
               bg_color, bold=True, size=FONT_SIZE_TITLE)
    # ... остальное
    _add_label(text_frame, price_str,
               bg_color, bold=True, size=FONT_SIZE_HEADER, align="e")


def _add_label(parent, text, bg_color, bold=False,
               size=FONT_SIZE_NORMAL, align="w"):
    """Добавляет метку с текстом."""
    tk.Label(parent, text=text, font=font(size, bold=bold),
             bg=bg_color, anchor=align).pack(fill="x")


def _indicator(qty):
    """Индикатор «много/мало» (порог 5)."""
    return "много" if qty > 5 else "мало"
