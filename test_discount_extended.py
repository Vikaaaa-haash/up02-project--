"""Расширенные тесты алгоритма скидки (ДЗ, вариант 11)."""
from datetime import datetime
from discount import calculate_price_with_discount


def run_extended_tests():
    """5 дополнительных тестов на разные даты и товары."""

    print("=" * 70)
    print("ДОПОЛНИТЕЛЬНЫЕ ТЕСТЫ (ДЗ, вариант 11)")
    print("=" * 70)

    # === ТЕСТ 1. Дата 15.11.2026 → предыдущий месяц = октябрь 2026 ===
    # В БД заказов за октябрь нет вообще → скидка применяется ко ВСЕМ товарам
    date1 = datetime(2026, 11, 15)
    result1 = calculate_price_with_discount(1, 2500000, date1)
    expected1 = 2500000 * 0.75  # 1875000
    status1 = "✅" if result1 == expected1 else "❌"
    print(f"{status1} Тест 1 (дата 15.11.2026, Toyota Camry): {int(result1)} "
          f"(ожидалось {int(expected1)}) — в октябре заказов нет → скидка")

    # === ТЕСТ 2. Дата 15.10.2026, товар id=4 (Audi A6) ===
    # Нет заказов в сентябре → скидка 25%
    date2 = datetime(2026, 10, 15)
    result2 = calculate_price_with_discount(4, 5000000, date2)
    expected2 = 5000000 * 0.75  # 3750000
    status2 = "✅" if result2 == expected2 else "❌"
    print(f"{status2} Тест 2 (Audi A6, 15.10.2026): {int(result2)} "
          f"(ожидалось {int(expected2)}) — нет заказов → скидка")

    # === ТЕСТ 3. Дата 15.10.2026, товар id=7 (Lada Vesta) ===
    # Нет заказов → скидка
    date3 = datetime(2026, 10, 15)
    result3 = calculate_price_with_discount(7, 1300000, date3)
    expected3 = 1300000 * 0.75  # 975000
    status3 = "✅" if result3 == expected3 else "❌"
    print(f"{status3} Тест 3 (Lada Vesta, 15.10.2026): {int(result3)} "
          f"(ожидалось {int(expected3)}) — нет заказов → скидка")

    # === ТЕСТ 4. Дата 15.10.2026, товар id=1 (Toyota Camry) ===
    # Есть заказ в сентябре → БЕЗ скидки
    date4 = datetime(2026, 10, 15)
    result4 = calculate_price_with_discount(1, 2500000, date4)
    expected4 = 2500000
    status4 = "✅" if result4 == expected4 else "❌"
    print(f"{status4} Тест 4 (Toyota Camry, 15.10.2026): {int(result4)} "
          f"(ожидалось {int(expected4)}) — есть заказ → без скидки")

    # === ТЕСТ 5. Дата 15.10.2026, товар id=2 (BMW X5) ===
    # Есть заказ в сентябре → БЕЗ скидки
    date5 = datetime(2026, 10, 15)
    result5 = calculate_price_with_discount(2, 5500000, date5)
    expected5 = 5500000
    status5 = "✅" if result5 == expected5 else "❌"
    print(f"{status5} Тест 5 (BMW X5, 15.10.2026): {int(result5)} "
          f"(ожидалось {int(expected5)}) — есть заказ → без скидки")

    # Итог
    passed = sum([
        result1 == expected1,
        result2 == expected2,
        result3 == expected3,
        result4 == expected4,
        result5 == expected5,
    ])
    print("=" * 70)
    print(f"Пройдено: {passed} / 5")


if __name__ == "__main__":
    run_extended_tests()