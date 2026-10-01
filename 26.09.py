from math import isfinite
from sys import float_info
from time import perf_counter


def finite_vector(values, name):
    result = [float(value) for value in values]
    if not all(isfinite(value) for value in result):
        raise ValueError(f"{name}: коэффициенты должны быть конечными числами.")
    return result


def thomas(lower, diagonal, upper, rhs):
    lower = finite_vector(lower, "lower")
    diagonal = finite_vector(diagonal, "diagonal")
    upper = finite_vector(upper, "upper")
    rhs = finite_vector(rhs, "rhs")
    n = len(diagonal)
    if n == 0 or len(rhs) != n or len(lower) != n - 1 or len(upper) != n - 1:
        raise ValueError("Нужны: diagonal и rhs длины n>=1, lower и upper длины n-1.")

    alpha = [0.0] * n
    beta = [0.0] * n

    for i in range(n):
        a = lower[i - 1] if i > 0 else 0.0
        c = upper[i] if i < n - 1 else 0.0
        previous_alpha = alpha[i - 1] if i > 0 else 0.0
        previous_beta = beta[i - 1] if i > 0 else 0.0
        denominator = diagonal[i] + a * previous_alpha
        row_scale = max(abs(a), abs(diagonal[i]), abs(c))
        if abs(denominator) <= 16 * float_info.epsilon * row_scale:
            raise ValueError(
                f"Шаг {i + 1}: нулевой или слишком малый знаменатель прогонки. "
                "Для этой системы нужен метод с выбором главного элемента."
            )
        alpha[i] = -c / denominator
        beta[i] = (rhs[i] - a * previous_beta) / denominator
        if not isfinite(alpha[i]) or not isfinite(beta[i]):
            raise ArithmeticError("Переполнение при прямом ходе прогонки.")

    x = [0.0] * n
    x[-1] = beta[-1]
    for i in range(n - 2, -1, -1):
        x[i] = alpha[i] * x[i + 1] + beta[i]
    if not all(isfinite(value) for value in x):
        raise ArithmeticError("Переполнение при обратном ходе прогонки.")
    return x


def simple_iteration(matrix, rhs, eps=1e-8, max_iterations=10000, x0=None):
    matrix = [finite_vector(row, "matrix") for row in matrix]
    rhs = finite_vector(rhs, "rhs")
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix) or len(rhs) != n:
        raise ValueError("Нужны квадратная матрица n>=1 и правая часть длины n.")
    if not isfinite(eps) or eps <= 0:
        raise ValueError("eps должна быть конечным положительным числом.")
    if not isinstance(max_iterations, int) or max_iterations < 1:
        raise ValueError("max_iterations должно быть положительным целым числом.")
    if any(matrix[i][i] == 0 for i in range(n)):
        raise ValueError("Для схемы Якоби элементы главной диагонали должны быть ненулевыми.")

    B = [
        [0.0 if i == j else -matrix[i][j] / matrix[i][i] for j in range(n)]
        for i in range(n)
    ]
    c = [rhs[i] / matrix[i][i] for i in range(n)]
    if not all(isfinite(value) for row in B for value in row) or not all(map(isfinite, c)):
        raise ArithmeticError("Переполнение при построении итерационной формы.")
    q = max(sum(abs(value) for value in row) for row in B)
    if q >= 1:
        raise ValueError(
            f"q={q:.6g} >= 1: достаточное условие сходимости в норме максимума "
            "не выполнено. Критерий Банаха в этой норме неприменим."
        )

    x = c.copy() if x0 is None else finite_vector(x0, "x0")
    if len(x) != n:
        raise ValueError("Начальное приближение x0 должно иметь длину n.")

    for iteration in range(1, max_iterations + 1):
        x_new = [sum(B[i][j] * x[j] for j in range(n)) + c[i] for i in range(n)]
        if not all(isfinite(value) for value in x_new):
            raise ArithmeticError("Переполнение в итерационном процессе.")
        difference = max(abs(x_new[i] - x[i]) for i in range(n))
        error_estimate = q / (1 - q) * difference
        if error_estimate <= eps:
            return x_new, iteration, q, error_estimate
        x = x_new

    raise RuntimeError(f"Точность eps={eps:g} не достигнута за {max_iterations} итераций.")


def residual_norm(matrix, x, rhs):
    return max(
        abs(sum(matrix[i][j] * x[j] for j in range(len(x))) - rhs[i])
        for i in range(len(x))
    )


def print_solution(x):
    for i, value in enumerate(x, start=1):
        print(f"x{i} = {value:.10f}")


def main():
    print("МЕТОД ПРОГОНКИ: пример со слайда 5")
    lower = [1, 1]
    diagonal = [2, 3, 2]
    upper = [1, 1]
    rhs = [4, 9, 8]

    start = perf_counter()
    x = thomas(lower, diagonal, upper, rhs)
    elapsed = perf_counter() - start
    print_solution(x)
    matrix = [[2, 1, 0], [1, 3, 1], [0, 1, 2]]
    print(f"Невязка ||Ax-b||_inf = {residual_norm(matrix, x, rhs):.3e}")
    print(f"Время выполнения: {elapsed:.6f} с")

    print("\nМЕТОД ПРОСТОЙ ИТЕРАЦИИ: пример со слайда 12")
    matrix = [[10, -1, 2], [-1, 11, -1], [2, -1, 10]]
    rhs = [6, 25, -11]
    eps = 1e-8

    start = perf_counter()
    x, iterations, q, estimate = simple_iteration(matrix, rhs, eps=eps)
    elapsed = perf_counter() - start
    print_solution(x)
    print(f"Заданная точность eps = {eps:g}")
    print(f"Коэффициент сжатия q = {q:.6f}")
    print(f"Количество итераций: {iterations}")
    print(f"Оценка погрешности по Банаху: {estimate:.3e}")
    print(f"Невязка ||Ax-b||_inf = {residual_norm(matrix, x, rhs):.3e}")
    print(f"Время выполнения: {elapsed:.6f} с")

if __name__ == "__main__":
    main()
