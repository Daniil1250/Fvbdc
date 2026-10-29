import sympy as sp

x = sp.Symbol('x')

# --- 1.1 Неравенство: x^3 + 10x - 5 < 0 ---
ineq1 = x**3 + 10*x - 5 < 0

# Получаем точный ответ в виде интервала
sol1 = sp.solve_univariate_inequality(ineq1, x, relational=False)
print(f"1.1 Точный ответ: {sol1}")

# Достаем границы интервала и округляем до 5 знаков
# Если ответ - интервал, у него есть .start и .end
left1 = sp.N(sol1.start, 5)
right1 = sp.N(sol1.end, 5)
print(f"1.1 Приближенный ответ (5 знаков): ({left1}; {right1})")


# --- 1.2 Система неравенств ---
# sqrt(1 + x^2) <= 5  И  x^3 - 2x > 1
ineq2_1 = sp.sqrt(1 + x**2) <= 5
ineq2_2 = x**3 - 2*x > 1
sys = sp.And(ineq2_1, ineq2_2)

# Получаем точный ответ
sol2 = sp.solve_univariate_inequality(sys, x, relational=False)
print(f"1.2 Точный ответ (система): {sol2}")

# Так как ответ для системы может быть сложным (объединение), 
# делаем проверку типа
if hasattr(sol2, 'start'):
    left2 = sp.N(sol2.start, 5)
    right2 = sp.N(sol2.end, 5)
    print(f"1.2 Приближенный ответ (5 знаков): ({left2}; {right2})")
else:
    # Если ответ сложный (например, Union), просто округляем его целиком
    print(f"1.2 Приближенный ответ (5 знаков): {sp.N(sol2, 5)}")
