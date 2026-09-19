import numpy as np

def householder_tridiagonalization(A):
    """
    Приводит симметричную матрицу A к трехдиагональному виду
    с помощью отражений Хаусхолдера.
    """
    n = A.shape[0]
    H_tridiag = A.copy().astype(float)

    for k in range(n - 2):
        x = H_tridiag[k+1:, k].copy()
        norm_x = np.linalg.norm(x)

        if norm_x < 1e-12:
            continue

        e1 = np.zeros_like(x)
        e1[0] = 1.0

        alpha = -np.sign(x[0]) * norm_x if x[0] != 0 else -norm_x
        v = x - alpha * e1

        if np.linalg.norm(v) < 1e-12:
            continue

        u = v / np.linalg.norm(v)
        H_prime = np.eye(n - k - 1) - 2 * np.outer(u, u)

        H = np.eye(n)
        H[k+1:, k+1:] = H_prime

        H_tridiag = H @ H_tridiag @ H
        H_tridiag[np.abs(H_tridiag) < 1e-12] = 0.0

    return H_tridiag


def eigenvalues_via_qr(T, tol=1e-12, max_iter=10000):
    """
    Находит собственные значения трёхдиагональной матрицы T
    с помощью QR-алгоритма (без сдвигов, для простоты).
    """
    T_curr = T.copy().astype(float)
    n = T_curr.shape[0]

    for _ in range(max_iter):
        # Проверка сходимости: поддиагональные элементы малы
        off_diag = np.array([T_curr[i+1, i] for i in range(n-1)])
        if np.all(np.abs(off_diag) < tol):
            break

        Q, R = np.linalg.qr(T_curr)
        T_curr = R @ Q

    return np.diag(T_curr)


# --- ПРИМЕР ИСПОЛЬЗОВАНИЯ ---

np.random.seed(42)
A = np.random.rand(5, 5)
A = (A + A.T) / 2  # симметричная

print("Исходная симметричная матрица A:")
print(np.round(A, 4))

# 1. Приводим к трёхдиагональному виду
T = householder_tridiagonalization(A)

print("\nТрехдиагональная матрица T:")
print(np.round(T, 4))

# 2. Собственные значения через QR-алгоритм
eig_qr = eigenvalues_via_qr(T)
eig_qr_sorted = np.sort(eig_qr)

print("\nСобственные значения (QR-алгоритм):")
print(np.round(eig_qr_sorted, 6))

# 3. Проверка через numpy (для сравнения)
eig_np = np.sort(np.linalg.eigvalsh(A))

print("\nСобственные значения (numpy.linalg.eigvalsh):")
print(np.round(eig_np, 6))

print("\nМаксимальное расхождение:", np.max(np.abs(eig_qr_sorted - eig_np)))

# 4. Собственные значения и векторы напрямую из трёхдиагональной матрицы
eigvals, eigvecs = np.linalg.eigh(T)

print("\nСобственные значения (eigh от T):")
print(np.round(np.sort(eigvals), 6))

print("\nСобственные векторы (eigh от T):")
print(np.round(eigvecs, 4))