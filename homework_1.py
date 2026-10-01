from statistics import median
from time import perf_counter


def lu_factor(a):
    n = len(a)
    lu = [list(map(float, row)) for row in a]
    p = list(range(n))
    for k in range(n):
        pivot = max(range(k, n), key=lambda i: abs(lu[i][k]))
        if abs(lu[pivot][k]) < 1e-14:
            raise ValueError("Матрица вырождена")
        lu[k], lu[pivot] = lu[pivot], lu[k]
        p[k], p[pivot] = p[pivot], p[k]
        for i in range(k + 1, n):
            lu[i][k] /= lu[k][k]
            for j in range(k + 1, n):
                lu[i][j] -= lu[i][k] * lu[k][j]
    return lu, p


def lu_solve(lu, p, b):
    n = len(lu)
    y = [0.0] * n
    x = [0.0] * n
    for i in range(n):
        y[i] = b[p[i]] - sum(lu[i][j] * y[j] for j in range(i))
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(lu[i][j] * x[j] for j in range(i + 1, n))) / lu[i][i]
    return x


def gauss_solve(a, b):
    n = len(a)
    u = [list(map(float, row)) for row in a]
    rhs = list(map(float, b))
    for k in range(n):
        pivot = max(range(k, n), key=lambda i: abs(u[i][k]))
        if abs(u[pivot][k]) < 1e-14:
            raise ValueError("Матрица вырождена")
        u[k], u[pivot] = u[pivot], u[k]
        rhs[k], rhs[pivot] = rhs[pivot], rhs[k]
        for i in range(k + 1, n):
            factor = u[i][k] / u[k][k]
            for j in range(k + 1, n):
                u[i][j] -= factor * u[k][j]
            rhs[i] -= factor * rhs[k]
            u[i][k] = 0.0
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (rhs[i] - sum(u[i][j] * x[j] for j in range(i + 1, n))) / u[i][i]
    return x


def main():
    a = [
        [0, 2, 1],
        [4, 3, 3],
        [8, 7, 9],
    ]
    right_sides = [
        [7, 19, 49],
        [2, 2, 10],
        [-1, 8, 18],
    ]
    lu, p = lu_factor(a)
    print("Фиксированная матрица A:")
    for row in a:
        print(row)
    for number, b in enumerate(right_sides, 1):
        x = lu_solve(lu, p, b)
        check = [sum(a[i][j] * x[j] for j in range(len(a))) for i in range(len(a))]
        assert all(abs(check[i] - b[i]) < 1e-9 for i in range(len(a)))
        assert all(abs(x[i] - y) < 1e-9 for i, y in enumerate(gauss_solve(a, b)))
        print(f"Система {number}: b = {b}, x = {[round(v, 6) for v in x]}")

    systems = right_sides * 5000
    gauss_times = []
    lu_times = []
    factor_times = []
    for _ in range(3):
        start = perf_counter()
        gauss_results = [gauss_solve(a, b) for b in systems]
        gauss_times.append(perf_counter() - start)

        start = perf_counter()
        lu, p = lu_factor(a)
        factor_times.append(perf_counter() - start)
        lu_results = [lu_solve(lu, p, b) for b in systems]
        lu_times.append(perf_counter() - start)
        assert all(
            all(abs(x[i] - y[i]) < 1e-9 for i in range(len(a)))
            for x, y in zip(gauss_results, lu_results)
        )

    gauss_time = median(gauss_times)
    lu_time = median(lu_times)
    print(f"\nСравнение для {len(systems)} систем с одной матрицей A:")
    print(f"Метод Гаусса (каждый раз заново): {gauss_time:.4f} с")
    print(f"LU-разложение (один раз):        {median(factor_times):.6f} с")
    print(f"LU-разложение + все решения:     {lu_time:.4f} с")
    print(f"Выигрыш по времени:              {gauss_time / lu_time:.2f} раза")


if __name__ == "__main__":
    main()
