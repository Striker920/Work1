
import math

mu = [2.0, 1 + math.sqrt(5)]

# Логистическое отображение
def f(m, n):
    x = 0.5
    for j in range(2 ** n):
        x = m * x * (1 - x)
    return x - 0.5

# Расчет константы Фейгенбаума
for n in range(2, 9):
    step = mu[-1] - mu[-2]
    left = mu[-1] + step * 0.02
    right = min(4.0, mu[-1] + step * 0.5)

    # Поиск интервала с корнем
    a = left
    for i in range(1, 1001):
        b = left + (right - left) * i / 1000
        if f(a, n) * f(b, n) < 0:
            break
        a = b
    else:
        raise ValueError("Корень не найден")

    # Метод бисекции
    for i in range(60):
        c = (a + b) / 2

        if f(a, n) * f(c, n) <= 0:
            b = c
        else:
            a = c

    mu.append((a + b) / 2)

    # Вычисление константы
    delta = (mu[-2] - mu[-3]) / (mu[-1] - mu[-2])

    print("n =", n, "mu =", round(mu[-1], 8),
          "delta =", round(delta, 8))

print("\nКонстанта Фейгенбаума =", round(delta, 8))
print("Теоретическое значение = 4.66920161")
