
import math


def f(x, mu, nu):
    if x < 0:
        raise ValueError("x не может быть отрицательным")
    return mu * math.sqrt(x) * (1 - nu * math.sqrt(x))


def stationary_point(mu, nu):
    if 1 + mu * nu == 0:
        raise ValueError("Нельзя вычислить точку")
    return (mu / (1 + mu * nu)) ** 2


def iterations(x, mu, nu, n):
    print(f"\nНачальное значение x0 = {x}")
    print(f"mu = {mu}, nu = {nu}")

    for i in range(n):
        x = f(x, mu, nu)
        print(f"x{i + 1} = {x:.8f}")

    return x


def run_tests():
    print("=== ТЕСТ 1: Вычисление функции ===")
    print("f(0.5) =", f(0.5, 3.9, 1))

    print("\n=== ТЕСТ 2: Неподвижная точка ===")
    mu = 3.9
    nu = 1
    x = stationary_point(mu, nu)
    print("x* =", x)
    print("f(x*) =", f(x, mu, nu))
    assert math.isclose(f(x, mu, nu), x, abs_tol=1e-10)

    print("\n=== ТЕСТ 3: Итерации ===")
    iterations(0.5, 3.9, 1, 30)

    print("\n=== ТЕСТ 4: Нулевое значение ===")
    assert f(0, 3.9, 1) == 0
    print("Успешно")

    print("\n=== ТЕСТ 5: x = 1 ===")
    assert f(1, 3.9, 1) == 0
    print("Успешно")

    print("\n=== ТЕСТ 6: Ошибка при x < 0 ===")
    try:
        f(-1, 3.9, 1)
        raise AssertionError("Ошибка не обнаружена")
    except ValueError:
        print("Успешно")

    print("\n=== ТЕСТ 7: Проверка неподвижной точки ===")
    for mu in [1, 2, 3, 3.9]:
        x = stationary_point(mu, 1)
        assert math.isclose(f(x, mu, 1), x, abs_tol=1e-10)
        print(f"mu = {mu}, x* = {x:.8f} - OK")

    print("\nВсе тесты пройдены!")


if __name__ == "__main__":
    run_tests()
