from sympy import symbols, reduce_inequalities, sqrt
x = symbols('x', real=True)
ineq1 = x**3 + 10*x - 5 < 0 sol1_exact = reduce_inequalities(ineq1, x) sol1_approx = sol1_exact.evalf(5)
print(sol1_exact) print(sol1_approx)
ineq2 = sqrt(1 + x2) <= 5 ineq3 = x3 - 2*x > 1 sol_sys_exact = reduce_inequalities([ineq2, ineq3], x) sol_sys_approx = sol_sys_exact.evalf(5)
print(sol_sys_exact) print(sol_sys_approx)
