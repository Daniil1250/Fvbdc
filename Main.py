import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# ЗАДАНИЕ 1
# ==========================================
print("--- ЗАДАНИЕ 1 ---")
x = sp.Symbol('x')

# 1.1 Неравенство x^3 + 10x - 5 < 0
# solveset ищет точное решение
ineq1 = x**3 + 10*x - 5 < 0
sol1 = sp.solveset(ineq1, x, domain=sp.S.Reals)
print(f"1.1 Точное решение: {sol1}")

# Извлекаем границы и округляем
# Для кубического уравнения корни могут быть сложными, поэтому evalf
# Получаем интервал
left1 = sp.N(sol1.start, 5)
right1 = sp.N(sol1.end, 5)
print(f"1.1 Приближенное решение (5 знаков): ({left1}, {right1})")


# 1.2 Система неравенств
ineq2_1 = sp.sqrt(1 + x**2) <= 5
ineq2_2 = x**3 - 2*x > 1
sys = sp.And(ineq2_1, ineq2_2)
sol2 = sp.solveset(sys, x, domain=sp.S.Reals)
print(f"1.2 Точное решение системы: {sol2}")

# Извлекаем границы для системы
left2 = sp.N(sol2.start, 5)
right2 = sp.N(sol2.end, 5)
print(f"1.2 Приближенное решение (5 знаков): ({left2}, {right2})")
print("\n")


# ==========================================
# ЗАДАНИЕ 2
# ==========================================
print("--- ЗАДАНИЕ 2 ---")
n = sp.Symbol('n', integer=True, positive=True)
x_n = (n**2 + n) / (3*n**2 + 2*n + 1)

# 1) Предел
a = sp.limit(x_n, n, sp.oo)
print(f"1) a = lim(n->oo) x_n = {a}")

# 2) n0(0.01)
epsilon = 0.01
n0 = 1
f_num = sp.lambdify(n, x_n, 'numpy')
a_float = float(a)

while abs(f_num(n0) - a_float) >= epsilon:
    n0 += 1
print(f"2) n0(0.01) = {n0}")

# 3) График
n_vals = np.arange(1, 30)
x_vals = f_num(n_vals)

plt.figure(figsize=(10, 6))
plt.plot(n_vals, x_vals, 'bo-', label='x_n')
plt.axhline(y=a_float, color='r', linestyle='--', label=f'Предел a={a_float:.4f}')
plt.axvline(x=n0, color='g', linestyle='-.', label=f'n0={n0}')
plt.grid(True, color='black', alpha=0.3)
plt.xlabel('n', color='black')
plt.ylabel('x_n', color='black')
plt.title('График последовательности x_n')
plt.legend()
plt.show()
print("\n")


# ==========================================
# ЗАДАНИЕ 3
# ==========================================
print("--- ЗАДАНИЕ 3 ---")
x = sp.Symbol('x')
f3 = x**2 * sp.ln(x + 1)
x0 = -0.5

# Производная
df3 = sp.diff(f3, x)
print(f"Производная f'(x): {df3}")

# Значение производной в x0
slope = df3.subs(x, x0)
print(f"f'(x0) = {slope}")

# Значение функции в x0
y0 = f3.subs(x, x0)
print(f"f(x0) = {y0}")

# Уравнение касательной
tangent = y0 + slope * (x - x0)
print(f"Уравнение касательной: y = {sp.simplify(tangent)}")

# График
f_num3 = sp.lambdify(x, f3, 'numpy')
t_num3 = sp.lambdify(x, tangent, 'numpy')

x_vals3 = np.linspace(-0.9, 0.5, 400)
plt.figure(figsize=(10, 6))
plt.plot(x_vals3, f_num3(x_vals3), label='f(x) = x^2 * ln(x+1)', color='blue')
plt.plot(x_vals3, t_num3(x_vals3), label=f'Касательная в x0={x0}', color='red', linestyle='--')
plt.plot(x0, float(y0), 'ko')
plt.grid(True, color='black', alpha=0.3)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('График функции и касательной')
plt.show()
print("\n")


# ==========================================
# ЗАДАНИЕ 4
# ==========================================
print("--- ЗАДАНИЕ 4 ---")
x = sp.Symbol('x')
f4 = (2*x**4 + 5*x + 2) / (x**3 - 2*x - 1)

# Точки разрыва
denom = x**3 - 2*x - 1
discontinuities = sp.solve(denom, x)
print("Точки разрыва:")
for d in discontinuities:
    if d.is_real:
        print(f"x = {sp.N(d, 4)}")
        
        limit_left = sp.limit(f4, x, d, '-')
        limit_right = sp.limit(f4, x, d, '+')
        print(f"  Предел слева: {limit_left}")
        print(f"  Предел справа: {limit_right}")

# Асимптоты
k = sp.limit(f4 / x, x, sp.oo)
b = sp.limit(f4 - k*x, x, sp.oo)
print(f"Наклонная асимптота: y = {k}x + {b}")

# Производная и экстремумы
df4 = sp.diff(f4, x)
crit_points = sp.solve(df4, x)
print("Критические точки (экстремумы):")
for c in crit_points:
    if c.is_real:
        print(f"x = {sp.N(c, 4)}")

# Определение интервалов возрастания/убывания (через знак производной)
# Для отчета достаточно указать точки, но можно написать словами, что на промежутках между ними знак меняется
print("Интервалы монотонности определяются сменой знака производной.")

# График
f_num4 = sp.lambdify(x, f4, 'numpy')
x_vals1 = np.linspace(-3, -1.3, 400)
x_vals2 = np.linspace(-0.6, 1.2, 400)
x_vals3 = np.linspace(1.4, 3, 400)

plt.figure(figsize=(12, 8))
plt.plot(x_vals1, f_num4(x_vals1), 'b', label='f(x)')
plt.plot(x_vals2, f_num4(x_vals2), 'b')
plt.plot(x_vals3, f_num4(x_vals3), 'b')

# Асимптота
x_asym = np.linspace(-3, 3, 100)
k_f = float(k)
b_f = float(b)
plt.plot(x_asym, k_f * x_asym + b_f, 'r--', label=f'Асимптота y={k_f:.2f}x+{b_f:.2f}')

# Вертикальные асимптоты
for d in discontinuities:
    if d.is_real:
        plt.axvline(x=float(d), color='g', linestyle=':', label=f'Разрыв x={float(d):.2f}')

plt.ylim(-20, 20)
plt.grid(True, color='black', alpha=0.3)
plt.legend()
plt.title('График функции, асимптоты и точки разрыва')
plt.show()
