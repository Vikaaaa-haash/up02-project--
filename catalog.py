"""Каталог автомобилей (вариант 11)."""
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

from config import DB_PATH
import database as db


# Цвета (по КИМ)
COLOR_BG = "#FFFFFF"
COLOR_HEADER = "#D2F6E7"
COLOR_ACCENT = "#70B2AF"
COLOR_HIGHLIGHT = "#ff8080"

FONT_FAMILY = "Calibri"


def create_product_card(parent, product):
    """
    Создаёт карточку автомобиля по макету.

    :param parent: родительский контейнер
    :param product: кортеж из БД (id, марка, модель, год, цена, количество, фото)
    """
    # Распаковка полей — вариант 11
    car_id = product[0]
    marka = product[1]
    model = product[2]
    year = product[3]
    price = product[4]
    qty = product[5]
    photo = product[6]

    # Подсветка, если количество ≤3
    bg_color = COLOR_HIGHLIGHT if qty <= 3 else "white"

    # Карточка — рамка
    card = tk.Frame(parent, bg=bg_color, bd=1, relief="solid")
    card.pack(fill="x", padx=10, pady=5)

    # === Изображение (слева) ===
    img_frame = tk.Frame(card, bg=bg_color)
    img_frame.pack(side="left", padx=10, pady=10)

    # Путь к фото
    image_path = f"resources/{photo}" if photo else "resources/picture.png"
    if not os.path.exists(image_path):
        image_path = "resources/picture.png"

    try:
        img = Image.open(image_path).resize((100, 100))
        photo_img = ImageTk.PhotoImage(img)
        img_label = tk.Label(img_frame, image=photo_img, bg=bg_color)
        img_label.image = photo_img   # ВАЖНО: сохраняем ссылку!
        img_label.pack()
    except Exception:
        tk.Label(img_frame, text="[ФОТО]", bg=bg_color,
                 width=10, height=5).pack()

    # === Текстовая часть (справа) ===
    text_frame = tk.Frame(card, bg=bg_color)
    text_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    # Марка | Модель (аналог «Производство | Наименование»)
    title = f"{marka} | {model}"
    tk.Label(text_frame, text=title, font=(FONT_FAMILY, 14, "bold"),
             bg=bg_color, anchor="w").pack(fill="x")

    # Год (аналог «Категория»)
    tk.Label(text_frame, text=f"Год: {year}",
             font=(FONT_FAMILY, 11), bg=bg_color, anchor="w").pack(fill="x")

    # Количество с индикатором
    indicator = "много" if qty > 5 else "мало"
    tk.Label(text_frame, text=f"Количество: {indicator} ({qty})",
             font=(FONT_FAMILY, 11), bg=bg_color, anchor="w").pack(fill="x")

    # Цена (справа)
    tk.Label(text_frame, text=f"{int(price)} руб.",
             font=(FONT_FAMILY, 14, "bold"),
             bg=bg_color, anchor="e").pack(fill="x")

    return card