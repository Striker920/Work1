"""Численное вычисление интеграла sin(x) / x на отрезке [1, 2].

Запуск: python integration_methods.py
Сторонние библиотеки не нужны. Углы задаются в радианах.

n — число частей, на каждой из которых применяется выбранная формула.
Поэтому Симпсон использует 2*n мелких интервалов, а «3/8» — 3*n.
При n=1 получаются формулы с доски без дополнительного разбиения.
Программа также сравнивает абсолютные погрешности и выбирает лучший метод.
"""

from math import sin, ulp


def f(x):
    return sin(x) / x

def integrate(func, a, b, n=1):
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n должно быть положительным целым числом")

    h = (b - a) / n
    result = {
        "Левые прямоугольники": 0.0,
        "Правые прямоугольники": 0.0,
        "Средние прямоугольники": 0.0,
        "Трапеции": 0.0,
        "Симпсон": 0.0,
        "3/8": 0.0,
    }

    for i in range(n):
        left = a + i * h
        right = a + (i + 1) * h
        middle = (left + right) / 2
        fl, fr, fm = func(left), func(right), func(middle)

        result["Левые прямоугольники"] += h * fl
        result["Правые прямоугольники"] += h * fr
        result["Средние прямоугольники"] += h * fm
        result["Трапеции"] += h * (fl + fr) / 2
        result["Симпсон"] += h * (fl + 4 * fm + fr) / 6
        result["3/8"] += h * (
            fl + 3 * func(left + h / 3)
            + 3 * func(left + 2 * h / 3) + fr
        ) / 8

    return result


def print_comparison(results, reference):
    """Печатает результаты, оценки погрешностей и наиболее точный метод."""
    errors = {
        name: abs(value - reference)
        for name, value in results.items()
    }

    print(f"{'Метод':24s} {'Значение':>18s} {'Абс. погрешность':>20s}")
    print("-" * 64)
    for name, value in results.items():
        print(f"{name:24s} {value:18.15f} {errors[name]:20.8e}")

    minimum_error = min(errors.values())
    # При очень малых ошибках различия вызваны округлением float.
    # ulp(reference) — расстояние между соседними числами около эталона.
    rounding_tolerance = 10 * ulp(reference)
    best_methods = [
        name for name, error in errors.items()
        if error - minimum_error <= rounding_tolerance
    ]

    if len(best_methods) == 1:
        print(f"\nМинимальная погрешность у метода: {best_methods[0]}")
    else:
        print("\nЛучшая точность с учётом округления: " + ", ".join(best_methods))

    print(f"Минимальная оценка погрешности: {minimum_error:.8e}")
    if minimum_error <= rounding_tolerance:
        print("Погрешность на уровне округления float; точнее сравнить нельзя.")


if __name__ == "__main__":
    a, b = 1.0, 2.0
    # Эталонное значение именно для интеграла sin(x)/x на [1, 2].
    # Это численное приближение, округлённое до точности float.
    reference = 0.6593299064355119
    print("Интеграл sin(x)/x на [1, 2]")
    print(f"Эталонное значение: {reference:.16f}")

    for n in (10, 1000):
        print(f"\nn = {n}")
        print_comparison(integrate(f, a, b, n), reference)

