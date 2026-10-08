"""Форма просмотра автомобиля (вариант 11)."""
import tkinter as tk
from tkinter import messagebox

from styles import (
    COLOR_MAIN_BG, COLOR_SECONDARY_BG, COLOR_ACCENT,
    FONT_SIZE_NORMAL, FONT_SIZE_HEADER, FONT_SIZE_TITLE, font,
)
from resources import get_product_image


class ViewForm:
    """Форма просмотра выбранного автомобиля."""

    def __init__(self, parent, product, on_add_to_order=None):
        """Инициализация формы."""
        self.product = product
        self.on_add_to_order = on_add_to_order

        self.window = tk.Toplevel(parent)
        self.window.title(f"Просмотр — {product[1]} {product[2]}")
        self.window.geometry("700x600")
        self.window.configure(bg=COLOR_MAIN_BG)

        self.build_ui()

    def build_ui(self):
        """Строит интерфейс формы."""
        # === Шапка ===
        header = tk.Frame(self.window, bg=COLOR_SECONDARY_BG, height=60)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text="КАРТОЧКА АВТОМОБИЛЯ",
            font=font(FONT_SIZE_TITLE, bold=True),
            bg=COLOR_SECONDARY_BG,
        ).pack(pady=15)

        # === Основная область ===
        main = tk.Frame(self.window, bg=COLOR_MAIN_BG)
        main.pack(fill="both", expand=True, padx=20, pady=20)

        # === Изображение (слева) ===
        img_frame = tk.Frame(main, bg=COLOR_MAIN_BG)
        img_frame.pack(side="left", padx=10)

        photo_name = self.product[6]
        if photo_name:
            image_path = f"resources/{photo_name}"
        else:
            image_path = "resources/picture.png"

        photo = get_product_image(image_path, size=(200, 200))
        if photo:
            img_label = tk.Label(img_frame, image=photo, bg=COLOR_MAIN_BG)
            img_label.image = photo
            img_label.pack()

        # === Информация (справа) ===
        info_frame = tk.Frame(main, bg=COLOR_MAIN_BG)
        info_frame.pack(side="left", fill="both", expand=True, padx=20)

        # === 6 полей формы ===
        self._add_field(info_frame, "Марка", self.product[1])
        self._add_field(info_frame, "Модель", self.product[2])
        self._add_field(info_frame, "Год выпуска", self.product[3])
        self._add_field(info_frame, "Цена", f"{int(self.product[4])} руб.")
        self._add_field(info_frame, "Количество", f"{self.product[5]} шт.")
        self._add_field(
            info_frame,
            "Описание",
            f"Автомобиль {self.product[1]} {self.product[2]}"
        )
                # === Поле ввода количества (ДЗ) ===
        tk.Label(
            info_frame,
            text="Количество для заказа:",
            font=font(FONT_SIZE_NORMAL, bold=True),
            bg=COLOR_MAIN_BG,
        ).pack(anchor="w", pady=(15, 0))

        self.qty_entry = tk.Entry(info_frame, width=10)
        self.qty_entry.pack(anchor="w", pady=5)

        tk.Button(
            info_frame,
            text="Проверить",
            command=self._check_qty,
            bg=COLOR_ACCENT,
            fg="white",
            font=font(FONT_SIZE_NORMAL),
            padx=10, pady=3,
            relief="flat",
        ).pack(anchor="w", pady=5)

        # === Кнопки ===
        btn_frame = tk.Frame(self.window, bg=COLOR_MAIN_BG)
        btn_frame.pack(fill="x", pady=10)

        tk.Button(
            btn_frame,
            text="Добавить в заказ",
            command=self.add_to_order,
            bg=COLOR_ACCENT,
            fg="white",
            font=font(FONT_SIZE_NORMAL),
            padx=15,
            pady=5,
            relief="flat",
            cursor="hand2",
        ).pack(side="left", padx=20)

        tk.Button(
            btn_frame,
            text="Назад",
            command=self.window.destroy,
            bg=COLOR_ACCENT,
            fg="white",
            font=font(FONT_SIZE_NORMAL),
            padx=15,
            pady=5,
            relief="flat",
            cursor="hand2",
        ).pack(side="right", padx=20)

    def _add_field(self, parent, label, value):
        """Добавляет поле в форму."""
        row = tk.Frame(parent, bg=COLOR_MAIN_BG)
        row.pack(fill="x", pady=3)

        tk.Label(
            row,
            text=f"{label}:",
            font=font(FONT_SIZE_NORMAL, bold=True),
            bg=COLOR_MAIN_BG,
            width=15,
            anchor="w",
        ).pack(side="left")

        tk.Label(
            row,
            text=str(value),
            font=font(FONT_SIZE_NORMAL),
            bg=COLOR_MAIN_BG,
            anchor="w",
        ).pack(side="left")

    def _check_qty(self):
        """Проверяет введённое количество (ДЗ)."""
        from error_handler import validate_positive_int

        ok, result = validate_positive_int(
            self.qty_entry.get(),
            "Количество"
        )

        if ok:
            messagebox.showinfo("OK", f"Количество: {result}")
        else:
            messagebox.showerror("Ошибка", result)

    def add_to_order(self):
        """Обработчик кнопки «Добавить в заказ»."""
        # 1. Проверка callback
        if not self.on_add_to_order:
            messagebox.showinfo("Информация", "Функция в разработке")
            return

        # 2. Проверка товара
        if not self.product:
            messagebox.showerror("Ошибка", "Автомобиль не выбран")
            return

        # 3. Попытка добавить в заказ
        try:
            self.on_add_to_order(self.product)
            messagebox.showinfo("Успех", "Автомобиль добавлен в заказ")
        except Exception as e:
            messagebox.showerror(
                "Ошибка заказа",
                f"Не удалось добавить автомобиль:\n{e}"
            )