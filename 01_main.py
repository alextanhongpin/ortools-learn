from ortools.linear_solver import pywraplp
from ortools.init import pywrapinit

# Problem statement:
# Maximize 3x + y subject to the following constraints:
# 0 <= x <= 1
# 0 <= y <= 2
# x + y <= 2

# GLOP is the ortools linear solver.
solver = pywraplp.Solver.CreateSolver("GLOP")

# Create the variables.
x = solver.NumVar(0, 1, "x")
y = solver.NumVar(0, 2, "y")

print("Number of variables =", solver.NumVariables())


# Create the linear constraint, 0 <= x + y <= 2
ct = solver.Constraint(0, 2, "ct")
ct.SetCoefficient(x, 1)
ct.SetCoefficient(y, 1)

print("Number of constraints =", solver.NumConstraints())


# Create the objective function, 3 * x + y.
objective = solver.Objective()
objective.SetCoefficient(x, 3)
objective.SetCoefficient(y, 1)
objective.SetMaximization()

solver.Solve()

print("Solution:")
print("Objective value =", objective.Value())
print("x =", x.solution_value())
print("y =", y.solution_value())
