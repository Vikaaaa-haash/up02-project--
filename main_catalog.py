"""Главное окно приложения с каталогом автомобилей."""
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import database as db
from catalog import create_product_card, FONT_FAMILY, COLOR_HEADER


APP_TITLE = "Каталог автомобилей — УП.02"


class CatalogWindow:
    """Главное окно каталога с поиском, фильтром и сортировкой."""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title(APP_TITLE)
        self.root.geometry("1100x700")

        # Переменные для поиска/фильтра/сортировки
        self.search_var = tk.StringVar()
        self.mark_var = tk.StringVar(value="Все марки")
        self.sort_var = tk.StringVar(value="Без сортировки")

        self.build_ui()
        self.refresh_catalog()

    def build_ui(self):
        """Строит интерфейс окна."""
        # === Шапка ===
        header = tk.Frame(self.root, bg=COLOR_HEADER)
        header.pack(fill="x")

        # Логотип
        try:
            logo = Image.open("resources/logo.png").resize((50, 50))
            logo_photo = ImageTk.PhotoImage(logo)
            logo_label = tk.Label(header, image=logo_photo, bg=COLOR_HEADER)
            logo_label.image = logo_photo
            logo_label.pack(side="left", padx=10, pady=5)
        except Exception:
            pass

        # Заголовок
        tk.Label(
            header, text="КАТАЛОГ АВТОМОБИЛЕЙ",
            font=(FONT_FAMILY, 16, "bold"), bg=COLOR_HEADER,
        ).pack(side="left", padx=10, pady=15)

        # === Панель управления (поиск, фильтр, сортировка) ===
        controls = tk.Frame(self.root, bg="#EFEFEF")
        controls.pack(fill="x", pady=5)

        # Поиск
        tk.Label(controls, text="Поиск:", bg="#EFEFEF",
                 font=(FONT_FAMILY, 11)).pack(side="left", padx=(10, 2))
        search_entry = tk.Entry(controls, textvariable=self.search_var, width=20)
        search_entry.pack(side="left", padx=2)
        self.search_var.trace_add("write", lambda *a: self.refresh_catalog())

        # Фильтр по марке
        tk.Label(controls, text="Марка:", bg="#EFEFEF",
                 font=(FONT_FAMILY, 11)).pack(side="left", padx=(20, 2))
        marks = ["Все марки"] + db.get_all_marks()
        mark_combo = ttk.Combobox(controls, textvariable=self.mark_var,
                                   values=marks, state="readonly", width=15)
        mark_combo.pack(side="left", padx=2)
        self.mark_var.trace_add("write", lambda *a: self.refresh_catalog())

        # Сортировка
        tk.Label(controls, text="Сортировка:", bg="#EFEFEF",
                 font=(FONT_FAMILY, 11)).pack(side="left", padx=(20, 2))
        sort_combo = ttk.Combobox(
            controls, textvariable=self.sort_var,
            values=["Без сортировки", "Цена ↑", "Цена ↓", "Марка А-Я"],
            state="readonly", width=15,
        )
        sort_combo.pack(side="left", padx=2)
        self.sort_var.trace_add("write", lambda *a: self.refresh_catalog())

        # === Каталог с прокруткой ===
        container = tk.Frame(self.root)
        container.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(container, bg="white", highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient="vertical",
                                   command=self.canvas.yview)
        self.catalog_frame = tk.Frame(self.canvas, bg="white")

        self.catalog_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )
        self.canvas.create_window((0, 0), window=self.catalog_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Прокрутка колёсиком
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _on_mousewheel(self, event):
        """Прокрутка колёсиком мыши."""
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def refresh_catalog(self):
        """Обновляет каталог с учётом поиска, фильтра и сортировки."""
        # 1. Очищаем все карточки
        for widget in self.catalog_frame.winfo_children():
            widget.destroy()

        # 2. Загружаем все товары
        products = db.get_all_products()

        # 3. Фильтр по поиску (по марке или модели)
        query = self.search_var.get().strip().lower()
        if query:
            products = [
                p for p in products
                if query in str(p[1]).lower() or query in str(p[2]).lower()
            ]

        # 4. Фильтр по марке
        mark = self.mark_var.get()
        if mark and mark != "Все марки":
            products = [p for p in products if p[1] == mark]

        # 5. Сортировка
        sort = self.sort_var.get()
        if sort == "Цена ↑":
            products.sort(key=lambda p: p[4])
        elif sort == "Цена ↓":
            products.sort(key=lambda p: p[4], reverse=True)
        elif sort == "Марка А-Я":
            products.sort(key=lambda p: p[1])

        # 6. Отображаем карточки
        for p in products:
            create_product_card(self.catalog_frame, p)

        # 7. Если ничего не найдено — показываем сообщение
        if not products:
            tk.Label(
                self.catalog_frame,
                text="Ничего не найдено",
                font=(FONT_FAMILY, 14), bg="white", fg="#888888",
            ).pack(pady=50)

    def run(self):
        """Запускает главный цикл приложения."""
        self.root.mainloop()


if __name__ == "__main__":
    CatalogWindow().run()