"""Главное окно приложения с каталогом автомобилей."""
import tkinter as tk
from tkinter import ttk
import database as db
from catalog import create_product_card, FONT_FAMILY, COLOR_HEADER


APP_TITLE = "Каталог автомобилей — УП.02"


class CatalogWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(APP_TITLE)
        self.root.geometry("900x700")

        self.build_ui()
        self.load_products()

"""Главное окно приложения с каталогом автомобилей."""
import tkinter as tk
from tkinter import ttk
import database as db
from catalog import create_product_card, FONT_FAMILY, COLOR_HEADER


APP_TITLE = "Каталог автомобилей — УП.02"


class CatalogWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(APP_TITLE)
        self.root.geometry("900x700")

        self.build_ui()
        self.load_products()

    def build_ui(self):
        # Заголовок
        header = tk.Frame(self.root, bg=COLOR_HEADER)
        header.pack(fill="x")
        tk.Label(header, text="КАТАЛОГ АВТОМОБИЛЕЙ",
                 font=(FONT_FAMILY, 16, "bold"),
                 bg=COLOR_HEADER).pack(pady=15)

        # Контейнер для canvas + scrollbar
        container = tk.Frame(self.root)
        container.pack(fill="both", expand=True)

        # Canvas
        self.canvas = tk.Canvas(container, bg="white", highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient="vertical",
                                   command=self.canvas.yview)
        self.catalog_frame = tk.Frame(self.canvas, bg="white")

        self.catalog_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.catalog_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # === ПРИВЯЗКА КОЛЁСИКА МЫШИ ===
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _on_mousewheel(self, event):
        """Обработка прокрутки колёсиком мыши (Windows)."""
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def load_products(self):
        products = db.get_all_products()
        for p in products:
            create_product_card(self.catalog_frame, p)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    CatalogWindow().run()

