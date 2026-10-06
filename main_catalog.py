"""Главное окно приложения с каталогом автомобилей."""
import os
import tkinter as tk
from tkinter import ttk
from styles import (
    COLOR_MAIN_BG, COLOR_SECONDARY_BG,
    FONT_SIZE_TITLE, FONT_SIZE_NORMAL, font,
)
from config import APP_TITLE
import database as db
from catalog import create_product_card
from resources import load_image_proportional, PATH_LOGO, PATH_ICON

def set_app_icon(root, icon_path):
    """Устанавливает иконку приложения кроссплатформенно."""
    from resources import load_image_proportional

    try:
        if os.name == "nt":   # Windows
            if os.path.exists(icon_path):
                root.iconbitmap(icon_path)
        else:                  # Linux/Mac
            png_path = icon_path.replace(".ico", ".png")
            icon_img = load_image_proportional(png_path, max_size=(32, 32))
            if icon_img:
                root.iconphoto(True, icon_img)
                root._icon_photo = icon_img   # сохраняем ссылку
    except Exception as e:
        print(f"Не удалось установить иконку: {e}")

class CatalogWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(APP_TITLE)
        self.root.geometry("1100x700")
        self.root.configure(bg=COLOR_MAIN_BG)

        # Переменные поиска/фильтра/сортировки
        self.search_var = tk.StringVar()
        self.mark_var = tk.StringVar(value="Все марки")
        self.sort_var = tk.StringVar(value="Без сортировки")

        set_app_icon(self.root, PATH_ICON)

        self.build_ui()
        self.refresh_catalog()

    def set_icon(self):
        """Устанавливает иконку приложения (кроссплатформенно)."""
        import os
        try:
            if os.name == "nt":   # Windows
                self.root.iconbitmap(PATH_ICON)
            else:                  # Linux/Mac
                icon_img = load_image_proportional(
                    PATH_ICON.replace(".ico", ".png"), max_size=(32, 32)
                )
                if icon_img:
                    self.root.iconphoto(True, icon_img)
                    self._icon_photo = icon_img
        except Exception as e:
            print(f"Не удалось установить иконку: {e}")

    def build_ui(self):
        # === Шапка с логотипом ===
        header = tk.Frame(self.root, bg=COLOR_SECONDARY_BG, height=80)
        header.pack(fill="x")
        header.pack_propagate(False)

        # Логотип с сохранением пропорций
        logo = load_image_proportional(PATH_LOGO, max_size=(60, 60))
        if logo:
            logo_label = tk.Label(header, image=logo, bg=COLOR_SECONDARY_BG)
            logo_label.image = logo
            logo_label.pack(side="left", padx=15)
        else:
            tk.Label(header, text="[ЛОГОТИП]",
                     bg=COLOR_SECONDARY_BG).pack(side="left", padx=15)

        # Заголовок по центру
        tk.Label(header, text="КАТАЛОГ АВТОМОБИЛЕЙ",
                 font=font(FONT_SIZE_TITLE, bold=True),
                 bg=COLOR_SECONDARY_BG).pack(expand=True)

        # === Панель управления ===
        controls = tk.Frame(self.root, bg=COLOR_SECONDARY_BG)
        controls.pack(fill="x", pady=5)

        tk.Label(controls, text="Поиск:", bg=COLOR_SECONDARY_BG,
                 font=font(11)).pack(side="left", padx=(10, 2))
        tk.Entry(controls, textvariable=self.search_var, width=20).pack(side="left", padx=2)
        self.search_var.trace_add("write", lambda *a: self.refresh_catalog())

        tk.Label(controls, text="Марка:", bg=COLOR_SECONDARY_BG,
                 font=font(11)).pack(side="left", padx=(20, 2))
        marks = ["Все марки"] + db.get_all_marks()
        ttk.Combobox(controls, textvariable=self.mark_var,
                     values=marks, state="readonly", width=15).pack(side="left", padx=2)
        self.mark_var.trace_add("write", lambda *a: self.refresh_catalog())

        tk.Label(controls, text="Сортировка:", bg=COLOR_SECONDARY_BG,
                 font=font(11)).pack(side="left", padx=(20, 2))
        ttk.Combobox(controls, textvariable=self.sort_var,
                     values=["Без сортировки", "Цена ↑", "Цена ↓", "Марка А-Я"],
                     state="readonly", width=15).pack(side="left", padx=2)
        self.sort_var.trace_add("write", lambda *a: self.refresh_catalog())

        # === Каталог ===
        container = tk.Frame(self.root, bg=COLOR_MAIN_BG)
        container.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(container, bg=COLOR_MAIN_BG, highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient="vertical",
                                   command=self.canvas.yview)
        self.catalog_frame = tk.Frame(self.canvas, bg=COLOR_MAIN_BG)
        self.catalog_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        self.canvas.create_window((0, 0), window=self.catalog_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def refresh_catalog(self):
        for widget in self.catalog_frame.winfo_children():
            widget.destroy()

        products = db.get_all_products()

        query = self.search_var.get().strip().lower()
        if query:
            products = [p for p in products
                        if query in str(p[1]).lower() or query in str(p[2]).lower()]

        mark = self.mark_var.get()
        if mark and mark != "Все марки":
            products = [p for p in products if p[1] == mark]

        sort = self.sort_var.get()
        if sort == "Цена ↑":
            products.sort(key=lambda p: p[4])
        elif sort == "Цена ↓":
            products.sort(key=lambda p: p[4], reverse=True)
        elif sort == "Марка А-Я":
            products.sort(key=lambda p: p[1])

        for p in products:
            create_product_card(self.catalog_frame, p)

        if not products:
            tk.Label(self.catalog_frame, text="Ничего не найдено",
                     font=font(14), bg=COLOR_MAIN_BG,
                     fg="#888888").pack(pady=50)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    CatalogWindow().run()