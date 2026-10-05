"""Тестирование алгоритма скидки (вариант 11 — Автомобили)."""
from datetime import datetime
from discount import calculate_price_with_discount


def run_tests():
    """Прогон тестов."""
    date = datetime(2026, 10, 15)  # → предыдущий месяц = сентябрь 2026

    # Заказы в сентябре 2026:
    #   товар_id=1 (Toyota Camry)     — заказ 15.09
    #   товар_id=2 (BMW X5)           — заказ 20.09
    #   товар_id=3 (Mercedes E-Class) — заказ 25.09
    # Остальные (4, 5, 6, 7) — заказов нет → скидка 25%
    test_cases = [
        (1, 2500000, 2500000, "Toyota Camry — есть заказ 15.09"),
        (2, 5500000, 5500000, "BMW X5 — есть заказ 20.09"),
        (3, 4000000, 4000000, "Mercedes E-Class — есть заказ 25.09"),
        (4, 5000000, 3750000, "Audi A6 — нет заказов → 25% скидка"),
        (5, 1200000, 900000,  "Kia Rio — нет заказов → скидка"),
        (6, 1500000, 1125000, "Hyundai Solaris — нет заказов → скидка"),
        (7, 1300000, 975000,  "Lada Vesta — нет заказов → скидка"),
    ]

    print("=" * 70)
    print("ТЕСТИРОВАНИЕ АЛГОРИТМА СКИДКИ (вариант 11)")
    print("=" * 70)

    passed = 0
    for product_id, price, expected, comment in test_cases:
        result = calculate_price_with_discount(product_id, price, date)
        status = "✅" if result == expected else "❌"
        if result == expected:
            passed += 1
        print(f"{status} Товар {product_id}: {price} → {int(result)} "
              f"(ожидалось {expected}) — {comment}")

    print("=" * 70)
    print(f"Пройдено: {passed} / {len(test_cases)}")


if __name__ == "__main__":
    run_tests()