```python
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# --- ЗАДАНИЕ 1 ---
x = sp.Symbol('x', real=True)
ineq1 = x**3 + 10*x - 5 < 0
exact_sol1 = sp.solve_univariate_inequality(ineq1, x, relational=False)
approx_sol1 = sp.N(exact_sol1, 5)
print(f"1.1: Точный: x < {exact_sol1}")
print(f"1.1: Приближенный: x < {approx_sol1}")

ineq2_1 = sp.sqrt(1 + x**2) <= 5
ineq2_2 = x**3 - 2*x > 1
sol2_1 = sp.solve_univariate_inequality(ineq2_1, x, relational=False)
sol2_2 = sp.solve_univariate_inequality(ineq2_2, x, relational=False)
system_sol = sp.Intersection(sol2_1, sol2_2).simplify()
print(f"1.2: Точный ответ системы: {system_sol}")

# --- ЗАДАНИЕ 2 ---
n = sp.Symbol('n', integer=True, positive=True)
x_n = (n**2 + n) / (3*n**2 + 2*n + 1)
a = sp.limit(x_n, n, sp.oo)
print(f"2.1: Предел a = {a}")

epsilon = 0.01
ineq = sp.Abs(x_n - a) < epsilon
n0_exact = sp.solve_univariate_inequality(ineq, n, relational=False)
n0_val = sp.ceiling(n0_exact.inf)
print(f"2.2: n0(0.01) = {n0_val}")

n_vals = np.arange(1, 30)
x_vals = [float(x_n.subs(n, i)) for i in n_vals]

plt.figure(figsize=(10, 6))
plt.plot(n_vals, x_vals, marker='o', linestyle='-', color='blue', label='\(x_n\)')
plt.axhline(y=float(a), color='red', linestyle='--', label=f'Предел a = {float(a):.5f}')
plt.axvline(x=float(n0_val), color='green', linestyle=':', label=f'\(n_0(0.01) = {int(n0_val)}\)')
plt.title('График последовательности \(x_n = \\frac{n^2+n}{3n^2+2n+1}\)')
plt.xlabel('n')
plt.ylabel('\(x_n\)')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

print("2.3: Предположения: монотонно возрастает, ограничена, сходится к a.")

# --- ЗАДАНИЕ 3 ---
x = sp.Symbol('x')
f = x**2 * sp.ln(x + 1)
x0 = -0.5
f_prime = sp.diff(f, x)
k = f_prime.subs(x, x0)
y0 = f.subs(x, x0)
tangent_line = y0 + k * (x - x0)
print(f"3: f'(x) = {f_prime}")
print(f"3: f'({x0}) = {k}")
print(f"3: Касательная: y = {sp.simplify(tangent_line)}")

x_vals3 = np.linspace(-0.99, 0.5, 400)
f_vals3 = [float(f.subs(x, val)) for val in x_vals3]
tangent_vals = [float(tangent_line.subs(x, val)) for val in x_vals3]

plt.figure(figsize=(10, 6))
plt.plot(x_vals3, f_vals3, label='f(x) = x^2 * ln(x+1)', color='blue')
plt.plot(x_vals3, tangent_vals, label=f'Касательная в x0={x0}', color='red', linestyle='--')
plt.scatter([x0], [float(y0)], color='black', zorder=5)
plt.title('График функции и касательной')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()

# --- ЗАДАНИЕ 4 ---
x = sp.Symbol('x')
f4 = (2*x**4 + 5*x + 2) / (x**3 - 2*x - 1)
denom = x**3 - 2*x - 1
discontinuities = sp.solve(denom, x)
print(f"4: Точки разрыва: {discontinuities}")

for pt in discontinuities:
    lim_left = sp.limit(f4, x, pt, '-')
    lim_right = sp.limit(f4, x, pt, '+')
    print(f"4: x={pt}: слева={lim_left}, справа={lim_right}")

k_asym = sp.limit(f4 / x, x, sp.oo)
b_asym = sp.limit(f4 - k_asym * x, x, sp.oo)
print(f"4: Наклонная асимптота: y = {k_asym}x + {b_asym}")

f_prime4 = sp.simplify(sp.diff(f4, x))
print(f"4: f'(x) = {f_prime4}")

critical_points = sp.solve(sp.numer(f_prime4), x)
real_critical_points = [pt.evalf() for pt in critical_points if pt.is_real]
print(f"4: Экстремумы (x): {real_critical_points}")

inc = sp.solve_univariate_inequality(f_prime4 > 0, x, relational=False)
dec = sp.solve_univariate_inequality(f_prime4 < 0, x, relational=False)
print(f"4: Возрастание: {inc}")
print(f"4: Убывание: {dec}")

x_vals4 = np.linspace(-3, 3, 1000)
f_vals4 = []
for val in x_vals4:
    if any(abs(val - float(pt)) < 0.01 for pt in discontinuities):
        f_vals4.append(np.nan)
    else:
        try:
            f_vals4.append(float(f4.subs(x, val)))
        except:
            f_vals4.append(np.nan)

plt.figure(figsize=(12, 8))
plt.plot(x_vals4, f_vals4, label='f(x)', color='blue')
x_asym = np.linspace(-5, 5, 100)
y_asym = float(k_asym) * x_asym + float(b_asym)
plt.plot(x_asym, y_asym, 'r--', label='Наклонная асимптота')
for pt in discontinuities:
    if pt.is_real:
        plt.axvline(x=float(pt), color='green', linestyle=':', label=f'Верт. асимптота x={float(pt):.2f}')
plt.ylim(-20, 20)
plt.title('График функции и асимптоты')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()
```
