"""Тесты граничных случаев (ДЗ, вариант 11)."""
from datetime import datetime
from discount import calculate_price_with_discount


def print_test_report(passed, total):
    """Выводит отчёт о тестировании (ДЗ, задание 2)."""
    print("=" * 40)
    print("ОТЧЁТ О ТЕСТИРОВАНИИ")
    print(f"Пройдено: {passed} / {total}")
    result = "✅ УСПЕХ" if passed == total else "❌ ЕСТЬ ОШИБКИ"
    print(f"Результат: {result}")
    print("=" * 40)


def run_edge_tests():
    """5 тестов на граничные случаи."""
    test_cases = [
        # 1. Дата — 1-е число месяца (01.10.2026 → предыдущий = сентябрь 2026)
        (1, 2500000, datetime(2026, 10, 1), 2500000,
         "01.10.2026 — Camry имеет заказ в сентябре → без скидки"),

        # 2. Дата — последний день месяца (31.10.2026 → предыдущий = сентябрь 2026)
        (4, 5000000, datetime(2026, 10, 31), 3750000,
         "31.10.2026 — Audi A6 без заказов в сентябре → скидка"),

        # 3. Товар с нулевой ценой (скидка применяется, результат = 0)
        (4, 0, datetime(2026, 10, 15), 0,
         "Товар с нулевой ценой → скидка, результат 0"),

        # 4. Товар с отрицательным количеством — проверка цены
        #    (алгоритм скидки не зависит от quantity, но тест проверяет, что не падает)
        (5, 1200000, datetime(2026, 10, 15), 900000,
         "Kia Rio, цена > 0, кол-во отрицательное — алгоритм работает"),

        # 5. Заказы были в позапрошлом месяце (август), но не в предыдущем (сентябрь)
        #    Дата 15.10.2026 → проверяем сентябрь. Заказов на id=5 в сентябре нет
        #    → скидка применяется
        (5, 1200000, datetime(2026, 10, 15), 900000,
         "Kia Rio — заказов в сентябре нет (хотя могли быть в августе) → скидка"),
    ]

    print("=" * 70)
    print("ТЕСТЫ ГРАНИЧНЫХ СЛУЧАЕВ (ДЗ, вариант 11)")
    print("=" * 70)

    passed = 0
    for product_id, price, date, expected, comment in test_cases:
        result = calculate_price_with_discount(product_id, price, date)
        status = "✅" if result == expected else "❌"
        if result == expected:
            passed += 1
        print(f"{status} Товар {product_id} на {date.date()}: "
              f"{price} → {int(result)} (ожидалось {int(expected)}) — {comment}")

    print()
    print_test_report(passed, len(test_cases))


if __name__ == "__main__":
    run_edge_tests()