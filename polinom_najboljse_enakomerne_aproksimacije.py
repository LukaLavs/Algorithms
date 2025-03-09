import math 
import matplotlib.pyplot as plt

def Mdot(A, B):
    """ Produkt matrik """
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def sign(x):
    return 1 if x > 0 else (-1 if x < 0 else 0)

def Linspace(a, b, n):
    return [a + (b-a)*i/(n-1) for i in range(n)]  

def Display(A, b):
    """" Prikaz maatričnega sistema """
    X = ["m"] + ["a" + str(i) for i in range(0, len(A[0]))]
    m = len(A)//2
    for i in range(len(A)):
        if i == m:
            print([f"{A[i][j]:.3f}" for j in range(len(A[0]))],"\t", "x ", f"[{X[i]}]", "\t","= ", f"[{b[i]:.3f}]")
        else:
            print([f"{A[i][j]:.3f}" for j in range(len(A[0]))],"\t","  ", f"[{X[i]}]", "\t", "  ", f"[{b[i]:.3f}]")

def Householder(A, b=None):
    """ QR razcep, Householderjeva zrcaljenja """
    if b:
        QTb = [[bi] for bi in b]
    m, n = len(A), len(A[0])
    Q = [[1 if i == j else 0 for j in range(m)] for i in range(m)]
    R = [row[:] for row in A]
    for k in range(n):
        x = [R[i][k] for i in range(k, m)]
        norm_x = (sum(xi**2 for xi in x))**0.5
        if norm_x == 0:
            continue
        sign = -1 if x[0] < 0 else 1
        x[0] += sign * norm_x  
        norm_u = (sum(xi**2 for xi in x))**0.5
        u = [xi / norm_u for xi in x]
        P = [[-2 * u[i] * u[j] for j in range(len(u))] for i in range(len(u))]
        P_full = [[1 if i == j else 0 for j in range(m)] for i in range(m)]
        for i in range(len(u)):
            for j in range(len(u)):
                P_full[k + i][k + j] += P[i][j]
        R = Mdot(P_full, R)
        Q = Mdot(Q, P_full)
        if b:
            QTb = Mdot(P_full, QTb)
    if b: 
        QTb = [QTb[i][0] for i in range(len(QTb))]
        return Q, R, QTb
    return Q, R

def Ux(U, y):
    """ Reši sistem Ux = y, kjer je U zgornje trikotniška matrika """
    n = len(y)
    x = [0 for i in range(len(y))]  
    for i in range(len(y)-1, -1, -1):
        x[i] = (y[i] - sum(U[i][k]*x[k] for k in range(i+1, n))) / U[i][i]
    return x

def QR_solve(A, b):
    """ Rešitev sistema Ax = b z QR razcepom """
    Q, R, QTb = Householder(A, b)
    x = Ux(R, QTb)
    # Preveri rešitev:
    b_ = Mdot(A, [[i] for i in x])
    b_ = [b_[i][0] for i in range(len(b_))]
    print("\nAx = b je ~ekvivalentno:")
    Display(A, b)
    norm2 = sum((i - j)**2 for (i, j) in zip(b, b_))**0.5
    print(f"x = {x}, \nnorm2(Ax-b) = {norm2}\n")
    return x

def G(A):
    """ Pomožna funkcija, ki vrstice ai0, ai1, ai2, ..., ain
    spremeni v -ai0, -ai1, -ai2, -ai3^2, ..., -ain^n, 
    za vsak i """
    B = [[-A[i][j]**(j-1) if j > 2 else -A[i][j] 
          for j in range(len(A[0]))] 
         for i in range(len(A))]
    return B
   
def F(E, f):
    return [f(i) for i in E]

def grid_search_max(f, a, b, density=1000, stopping=1e3):
    """ funkcija poišče maximum za f na [a, b] """
    accuracy = 1e-16
    M = float("-inf")
    x = a
    x_prev = b # začetni približek
    stopping = 0
    while abs(x - x_prev) > accuracy:
        stopping += 1
        if stopping > 1e3: break
        T = Linspace(a, b, density)
        x_prev = x
        for t in T:
            v = abs(f(t))
            if v > M: 
                M = v
                x = t
        l = (b-a)/density
        a, b = x - l, x + l
    print(f"u = max(abs(r(x))) = {M}, x* = {x}\n")
    return x

def plot(f, p, a, b, accuracy=100):
    T = Linspace(a, b, (b-a)*accuracy)
    Y1 = [f(t) for t in T]
    Y2 = [p(t) for t in T]
    plt.plot(T, Y1, label="f(x)", color='blue')
    plt.plot(T, Y2, label="p*(x)", color='red')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graf')
    plt.legend()
    plt.grid(True)
    plt.show()

def p_n_e_a(E, f, q, w, draw=True, tolerance=1e-10, max_iterations=100):
    """ Polinom najboljše enakomerne aproksimacije.
    Iščemo optimalen p*(x) = a0 + a1*x + ... + an*x^n 
    na intervalu [q, w] """
    # E = [množica n + 2 točk, kjer je n stopnja polinoma p*]
    n = len(E)
    print(f"\nE0 = {E}\n")
    for _ in range(1, max_iterations):
        # Ustvarimo matriko za sistem enačb f(xi) - p*(xi) = m * (-1)^i
        A = [[(-1)**i if j == 0 else (1 if j == 1 else E[i]) for j in range(n)] for i in range(n)]
        A = G(A)
        
        # Rešimo sistem Ax = -F(E), kjer je x = [m, a0, a1, ..., an]
        b = F(E, f)
        b = [-i for i in b]
        x = QR_solve(A, b)
        koef = x[1:]
        m = x[0]
        
        # Definirajmo ostanek r(x) = f(x) - p*(x)
        def r(x):
            return f(x) - sum(koef[i]*x**i for i in range(len(koef)))
        
        # Poiščimo tak u \in [q, w], da |r(u)| = max(|r(x)|; x \in [q, w])
        u = grid_search_max(r, q, w)
        
        # Preverimo ali smemo zaključiti
        if abs(abs(r(u)) - abs(m)) < tolerance:
            print(f"koef = {koef}")
            print(f"E{_ -1} = {E}")
            if draw:
                def p(x):
                    return sum(koef[i]*x**i for i in range(len(koef)))
                plot(f, p, q, w)
            print(f"koef = {koef}\nE = {E}")
            return koef, E
        
        # Poiščimo tista e := E_i in e_ := E_{i+1}, da bo u med njima,
        # zamenjajmo u in tisti E_j, ki da enak predznak skozi r
        e = E[0]
        index_e = 0
        if u < e or u > E[-1]: print("Napaka, u < E[0] ali u > E[-1]"); break
        # Če u < e or u > E[-1], nisem prepričan kaj storiti, algoritem zaključim
        for i in range(1, len(E)):
            if u < E[i]:
                e_ = E[i]
                index_e_ = i
                break
            e = E[i]
            index_e = i
        
        if sign(r(e)) == sign(r(u)):
            index = index_e
        else:
            index = index_e_
            
        E[index] = u
        print(f"E{_} = {E}\n")
        
    print(f"Zaključili zaradi max_iterations ali prekinitve\nkoef = {koef}\nE{_} = {E}")
    if draw:
        def p(x):
            return sum(koef[i]*x**i for i in range(len(koef)))
        plot(f, p, q, w)
    return koef, E
        
##################################################
##################################################  

def f(x):
    return math.sin(5*x)/4 + math.sin(x)

# Polinom stopnje n, na [0, 1]:  
n = 5   
p_n_e_a(Linspace(0, 1, n + 2), f, 0, 1, draw=True)
