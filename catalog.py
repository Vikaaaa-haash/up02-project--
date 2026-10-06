"""Каталог автомобилей (вариант 11)."""
import tkinter as tk
from styles import (
    COLOR_MAIN_BG, COLOR_HIGHLIGHT,
    FONT_SIZE_NORMAL, FONT_SIZE_HEADER, FONT_SIZE_TITLE,
    font,
)
from resources import get_product_image


def create_product_card(parent, product):
    """Создаёт карточку автомобиля по макету."""
    # Распаковка полей — вариант 11
    car_id = product[0]
    marka = product[1]
    model = product[2]
    year = product[3]
    price = product[4]
    qty = product[5]
    photo = product[6]

    # Подсветка ≤3
    bg_color = COLOR_HIGHLIGHT if qty <= 3 else COLOR_MAIN_BG

    # Карточка — рамка
    card = tk.Frame(parent, bg=bg_color, bd=1, relief="solid")
    card.pack(fill="x", padx=10, pady=5)

    # === Изображение (слева) — через resources.py ===
    img_frame = tk.Frame(card, bg=bg_color)
    img_frame.pack(side="left", padx=10, pady=10)

    # Путь к фото
    image_path = f"resources/{photo}" if photo else "resources/picture.png"

    # Загружаем фото (или заглушку — автоматически!)
    photo_img = get_product_image(image_path, size=(100, 100))
    if photo_img:
        img_label = tk.Label(img_frame, image=photo_img, bg=bg_color)
        img_label.image = photo_img   # ВАЖНО: сохраняем ссылку!
        img_label.pack()
    else:
        tk.Label(img_frame, text="[НЕТ ФОТО]", bg=bg_color,
                 width=10, height=5).pack()

    # === Текстовая часть (справа) ===
    text_frame = tk.Frame(card, bg=bg_color)
    text_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    # Марка | Модель
    tk.Label(text_frame, text=f"{marka} | {model}",
             font=font(FONT_SIZE_TITLE, bold=True),
             bg=bg_color, anchor="w").pack(fill="x")

    # Год
    tk.Label(text_frame, text=f"Год: {year}",
             font=font(FONT_SIZE_NORMAL),
             bg=bg_color, anchor="w").pack(fill="x")

    # Количество
    indicator = "много" if qty > 5 else "мало"
    tk.Label(text_frame, text=f"Количество: {indicator} ({qty})",
             font=font(FONT_SIZE_NORMAL),
             bg=bg_color, anchor="w").pack(fill="x")

    # Цена
    tk.Label(text_frame, text=f"{int(price)} руб.",
             font=font(FONT_SIZE_HEADER, bold=True),
             bg=bg_color, anchor="e").pack(fill="x")

    return card