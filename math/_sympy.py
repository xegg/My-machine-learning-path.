from sympy import symbols, init_printing, solveset, Eq, Matrix
from sympy.solvers.solveset import linsolve

x, y, z = symbols('x y z')
init_printing(use_unicode=True)
print(solveset(Eq(x**2, 1), x))
print(solveset(x**2-1, x))

# solve linear system
# list of equations form
print(linsolve([x + y + z - 1, x + y + 2*z - 3 ], (x, y, z)))

# Augmented Matrix Form:
print(linsolve(Matrix(([1, 1, 1, 1], [1, 1, 2, 3])), (x, y, z)))

# A*x = b Form
M = Matrix(((1, 1, 1, 1), (1, 1, 2, 3)))
system = A, b = M[:, :-1], M[:, -1]
print(linsolve(system, x, y, z))
