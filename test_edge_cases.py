"""Тесты на некорректные данные (ДЗ)."""
from catalog import _indicator


def test_edge_cases():
    """Проверяет поведение на некорректных данных."""
    cases = [
        (None, "мало", "None — не число, но не падает"),
        ("10", "мало", "строка — не число, но не падает"),
        (0.5, "мало", "дробное — 0.5 ≤ 5"),
    ]

    print("=" * 60)
    print("ТЕСТЫ НА НЕКОРРЕКТНЫЕ ДАННЫЕ")
    print("=" * 60)

    passed = 0
    for qty, expected, comment in cases:
        try:
            result = _indicator(qty)
            status = "✅" if result == expected else "❌"
            if result == expected:
                passed += 1
            print(f"{status} qty={qty!r}: {result} — {comment}")
        except Exception as e:
            print(f"❌ qty={qty!r}: ОШИБКА — {e}")
            # Не увеличиваем passed

    print("=" * 60)
    print(f"Пройдено: {passed} / {len(cases)}")


if __name__ == "__main__":
    test_edge_cases()