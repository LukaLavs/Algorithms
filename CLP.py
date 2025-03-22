from pulp import LpMinimize, LpProblem, LpVariable, lpSum, value
import random

def print_matrix(matrix):
    """Nicely prints a 2D matrix with aligned columns."""
    col_widths = [max(len(str(item)) for item in col) for col in zip(*matrix)]
    for row in matrix:
        print("  ".join(f"{str(item):>{col_widths[i]}}" for i, item in enumerate(row)))
   
def traveling_salesman(C):
    """ 
    Parameters:
    C (list): matrix of costs, where c_ij is the cost for traveling from i to j
    """       
    n = len(C)
    p = LpProblem('Traveling_salesman_problem', LpMinimize)
    # Variables
    x = {(i, j): LpVariable(f"x_{i}_{j}", cat="Binary") for i in range(n) for j in range(n)}
    y = {i: LpVariable(f"y_{i}", cat="Integer") for i in range(n)}
    # Add objective function
    p += lpSum(C[i][j] * x[i, j] for i in range(n) for j in range(n))
    # Constraints
    for _ in range(n):
        p += lpSum(x[i, _] for i in range(n)) == 1
        p += lpSum(x[_, j] for j in range(n)) == 1
    p += y[0] == 0
    for i in range(n):
        for j in range(1, n):
            p += y[j] - y[i] >= 1 - n + n*x[i, j]
    # Solve the problem   
    p.solve()        
    # Extract selected edges (route)
    selected_edges = [(i, j) for i in range(n) for j in range(n) if value(x[i, j]) == 1]
    # Extract total cost of the route
    total_cost = value(p.objective)
    # Print results
    print("######### RESULTS ##############")
    print("Optimal route (edges):", selected_edges, "\n")
    print("Total cost of the route:", total_cost, "\n")
    print("Matrix C:")
    print_matrix(C)
    
    
 
n = 20  # Number of cities
C = [[0 if i == j else random.randint(10, 100) for j in range(n)] for i in range(n)]
traveling_salesman(C)