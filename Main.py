import sympy as sp

x = sp.Symbol('x')

# 1.1 Неравенство x^3 + 10x - 5 < 0
ineq = x**3 + 10*x - 5 < 0
exact_ineq = sp.solve_univariate_inequality(ineq, x, relational=False)
approx_ineq = [sp.N(bound, 5) for bound in exact_ineq.args]

print("1. Точный ответ (неравенство):", exact_ineq)
print("   Приближенный (5 знаков):", approx_ineq)

# 1.2 Система неравенств
# sqrt(1 + x^2) <= 5  и  x^3 - 2x > 1
sys_ineq = sp.And(sp.sqrt(1 + x**2) <= 5, x**3 - 2*x > 1)
exact_sys = sp.solve_univariate_inequality(sys_ineq, x, relational=False)
approx_sys = [sp.N(bound, 5) for bound in exact_sys.args]

print("2. Точный ответ (система):", exact_sys)
print("   Приближенный (5 знаков):", approx_sys)
