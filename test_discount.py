"""Тестирование алгоритма скидки (вариант 11 — Автомобили)."""
from datetime import datetime
from discount import calculate_price_with_discount


def run_tests():
    """Расширенное тестирование алгоритма скидки."""
    test_cases = [
        # (product_id, price, date, expected, comment)
        # --- Базовые тесты (дата 15.10.2026 → предыдущий месяц = сентябрь 2026) ---
        (1, 2500000, datetime(2026, 10, 15), 2500000, "Toyota Camry — есть заказ 15.09"),
        (2, 5500000, datetime(2026, 10, 15), 5500000, "BMW X5 — есть заказ 20.09"),
        (3, 4000000, datetime(2026, 10, 15), 4000000, "Mercedes E-Class — есть заказ 25.09"),
        (4, 5000000, datetime(2026, 10, 15), 3750000, "Audi A6 — нет заказов → скидка"),
        (5, 1200000, datetime(2026, 10, 15), 900000,  "Kia Rio — нет заказов → скидка"),
        (6, 1500000, datetime(2026, 10, 15), 1125000, "Hyundai Solaris — нет заказов → скидка"),
        (7, 1300000, datetime(2026, 10, 15), 975000,  "Lada Vesta — нет заказов → скидка"),

        # --- Новые тесты (разные даты) ---
        # Дата 15.11.2026 → предыдущий месяц = октябрь 2026. В БД заказов за октябрь нет
        # → скидка применяется ко ВСЕМ товарам
        (1, 2500000, datetime(2026, 11, 15), 1875000, "Camry — в октябре заказов нет → скидка"),
        (2, 5500000, datetime(2026, 11, 15), 4125000, "BMW X5 — в октябре заказов нет → скидка"),

        # Дата 01.09.2026 → предыдущий месяц = август 2026. Заказов за август нет
        # → скидка применяется
        (4, 5000000, datetime(2026, 9, 1), 3750000, "Audi A6 — в августе заказов нет → скидка"),
    ]

    print("=" * 70)
    print("РАСШИРЕННОЕ ТЕСТИРОВАНИЕ АЛГОРИТМА СКИДКИ")
    print("=" * 70)

    passed = 0
    for product_id, price, date, expected, comment in test_cases:
        result = calculate_price_with_discount(product_id, price, date)
        status = "✅" if result == expected else "❌"
        if result == expected:
            passed += 1
        print(f"{status} Товар {product_id} на {date.date()}: "
              f"{price} → {int(result)} (ожидалось {int(expected)}) — {comment}")

    print("=" * 70)
    print(f"Пройдено: {passed} / {len(test_cases)}")


if __name__ == "__main__":
    run_tests()