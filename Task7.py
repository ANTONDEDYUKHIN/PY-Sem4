# найти корни квадратного уравнения 2мя способами.
# ax^2 + bx + c = 0, a=2, b=2, c=1
from sympy import *
from sympy.plotting import plot
from sympy.solvers.inequalities import solve_univariate_inequality
f = 4*x**4 - 65*x**2 +16
solve(f)
