def f(x, nu, mu):
    if x < 0:
        raise ValueError("x должен быть неотрицательным")
    return mu * x**0.5 * (1 - nu * x**0.5)


def stationary_point(nu, mu):
    return (mu / (mu * nu + 1))**2


x = float(input("Начальное x = "))
mu = float(input("mu = "))
nu = float(input("nu = "))
n = int(input("Количество итераций = "))

print("Значение функции:", f(x, nu, mu))
print("Неподвижная точка:", stationary_point(nu, mu))

values = [x]

for i in range(n):
    x = f(x, nu, mu)
    values.append(x)

for i, value in enumerate(values):
    print(f"x[{i}] = {value:.10f}")