"""Обработка исключений для проекта УП.02."""
from tkinter import messagebox


def safe_call(func, *args, **kwargs):
    """
    Безопасный вызов функции с обработкой ошибок.

    :param func: функция для вызова
    :param args: позиционные аргументы
    :param kwargs: именованные аргументы
    :return: результат func или None при ошибке
    """
    try:
        return func(*args, **kwargs)
    except FileNotFoundError as e:
        messagebox.showerror("Ошибка файла", f"Файл не найден:\n{e}")
    except ConnectionError as e:
        messagebox.showerror("Ошибка соединения", f"Нет связи с БД:\n{e}")
    except ValueError as e:
        messagebox.showwarning("Ошибка данных", f"Некорректное значение:\n{e}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка:\n{e}")
    return None


def validate_positive_int(value, field_name="Значение"):
    """
    Проверяет, что значение — положительное целое число.

    :param value: строка для проверки
    :param field_name: название поля (для сообщения)
    :return: (True, число) или (False, текст ошибки)
    """
    try:
        number = int(value)
        if number <= 0:
            return (False, f"{field_name} должно быть больше нуля")
        return (True, number)
    except (ValueError, TypeError):
        return (False, f"{field_name} должно быть целым числом")