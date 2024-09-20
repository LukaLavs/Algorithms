from fractions import Fraction

def frac(x, y): 
    return Fraction(x, y)

def make_a_table(A, b, c):
    m, n = len(A), len(c)
    table = [[0]*(n + m + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            table[i][j] = A[i][j]
        table[i][n + i] = 1
        table[i][-1] = b[i]    
    for j in range(n):
        table[-1][j] = c[j]
    return table

def extract_solution(table, m, n):
    solution = [0] * (n + m)
    for i in range(m):
        for j in range(n + m):
            # Če je x-i v nekem pogoju bazna, ima v tabeli vrednost 1 in se v drugih pogojih ter funkciji ne pojavi
            if table[i][j] == 1 and all(table[k][j] == 0 for k in range(m + 1) if k != i):
                solution[j] = table[i][-1]
                break
    optimal_value = -table[-1][-1]
    solution, dual_values = solution[:n], solution[n:]
    print(f"Optimal solution: {list(map(str,solution))} == {[round(float(s), 4) for s in solution]}")
    print(f"Dual variable values: {list(map(str,dual_values))} == {[round(float(s), 4) for s in dual_values]}")
    print(f"Optimal value: {optimal_value} == {round(float(optimal_value), 4)}")
    return None

def convert_to_fractions(A, b, c):
    A = [[Fraction(el) if not isinstance(el, Fraction) else el for el in row] for row in A]
    b = [Fraction(el) if not isinstance(el, Fraction) else el for el in b]
    c = [Fraction(el) if not isinstance(el, Fraction) else el for el in c]
    return A, b, c

def simplex_method(A, b, c):
    A, b, c = convert_to_fractions(A, b, c)
    m, n = len(A), len(c)
    table = make_a_table(A, b, c)
    while True:
        # Izberemo x-i po pravilu največjega koeficienta:
        pivot_col = max(range(n + m), key=lambda j: table[-1][j])
        # če so vse vrednosti v funkciji negativne, imamo optimalno rešitev:
        if table[-1][pivot_col] <= 0:
            break
        # izberemo pogoj, ki izbrani x-i najstrožje omejuje:
        pivot_row = min(
            (i for i in range(m) if table[i][pivot_col] > 0),
            key=lambda i: table[i][-1] / table[i][pivot_col],
            default=None
            )     
        if pivot_row is None: 
            raise ValueError("Linearni program je neomejen")
        pivot_value = table[pivot_row][pivot_col]      
        for j in range(n + m + 1):
            table[pivot_row][j] /= pivot_value    
        # x-i vstopi v bazo, druge pogoje ustrezno prepišemo
        for i in range(m + 1):
            if i != pivot_row:
                row_factor = table[i][pivot_col]
                for j in range(n + m + 1):
                    table[i][j] -= row_factor * table[pivot_row][j]  
    return extract_solution(table, m, n)
        

###################################################################
###################################################################
###################################################################
        
c = [400, 600, 480] 
A = [[1, 1, 1], [60, 80, 100], [240, 400, 320]] 
b = [50, 5000, 24000]

simplex_method(A, b, c)


print("\n")

c = [3, 2] 
A = [[2, Fraction(1, 99)], [Fraction(1, 99), Fraction(3, 2)], [Fraction(1, 9), Fraction(1, 99)]] 
b = [18, 42, 24]

simplex_method(A, b, c)
