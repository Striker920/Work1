from sympy import symbols, Eq, solve, simplify

A, B, C = symbols("A B C")
h = symbols("h", nonzero=True)  # h = b - a

equations = [
    Eq(A + B + C, h),
    Eq(B * h / 2 + C * h, h**2 / 2),
    Eq(B * (h / 2)**2 + C * h**2, h**3 / 3),
]

solution = solve(equations, (A, B, C))

for variable in (A, B, C):
    print(f"{variable} = {solution[variable]}")

# Проверяем решение подстановкой
for i, equation in enumerate(equations, start=1):
    residual = simplify((equation.lhs - equation.rhs).subs(solution))
    print(f"Уравнение {i}: разность частей = {residual}")