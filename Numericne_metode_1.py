def LU(A):
    """ LU razcep brez pivotiranja"""
    n = len(A)
    R = [A[i][:] for i in range(n)]
    for k in range(n):
        for i in range(k+1, n):
            R[i][k] /= R[k][k]
            for j in range(k+1, n):
                R[i][j] -= R[i][k] * R[k][j]
    
    L = [[1 if i == j else (R[i][j] if i >= j+1 else 0)
           for j in range(n)] for i in range(n)]
    U = [[R[i][j] if i <= j else 0 
          for j in range(n)] for i in range(n)]
    return L, U



def Cholesky(A):
    """ Cholesky razcep"""
    n = len(A)
    V = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        V[i][i] = (A[i][i] - sum([V[i][k]**2 for k in range(i)]))**0.5
        for j in range(i+1, n):
            V[j][i] = (A[j][i] - sum([V[j][k]*V[i][k] for k in range(i)])) / V[i][i]
    return V



def QR(A):
    """ QR razcep, Gram-Schmidt"""
    m, n = len(A), len(A[0])
    Q = [[0 for j in range(n)] for i in range(m)]
    R = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        q = [A[k][i] for k in range(m)]
        for j in range(i):
            R[j][i] = sum(Q[k][j] * A[k][i] for k in range(m))
            q = [q[k] - R[j][i] * Q[k][j] for k in range(m)]
        R[i][i] = sum(q[k]**2 for k in range(m))**0.5
        for k in range(m):
            Q[k][i] = q[k] / R[i][i]
    return Q, R



def Mdot(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def Givens(A, b=None):
    """ Givensove rotacije """
    if b:
        b = [[bi] for bi in b]
    m, n = len(A), len(A[0])
    R = [row[:] for row in A]
    Q = [[1 if i == j else 0 for j in range(m)] for i in range(m)]
    for k in range(n):
        for j in range(k+1, m):
            if R[j][k] != 0:
                r = (R[k][k]**2 + R[j][k]**2)**0.5
                c = R[k][k] / r
                s = R[j][k] / r
                G = [[1 if i == j else 0 for j in range(m)] for i in range(m)]
                G[k][k] = c
                G[j][j] = c
                G[k][j] = s
                G[j][k] = -s
                R = Mdot(G, R)
                Q = Mdot(G, Q)
                if b:
                    b = Mdot(G, b)
    Q = [list(row) for row in zip(*Q)]
    if b: return Q, R, b
    return Q, R



def Mdot(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def Householder(A, b=None):
    """ QR razcep, Householderjeva zrcaljenja """
    if b:
        b = [[bi] for bi in b]
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
            b = Mdot(P_full, b)
    if b: return Q, R, b
    return Q, R



def Ly(L, b):
    y = [0 for i in range(len(b))]
    for i in range(len(b)):
        y[i] = b[i] - sum(L[i][k]*y[k] for k in range(i))
    return y

def Ux(U, y):
    n = len(y)
    x = [0 for i in range(len(y))]  
    for i in range(len(y)-1, -1, -1):
        x[i] = (y[i] - sum(U[i][k]*x[k] for k in range(i+1, n))) / U[i][i]
    return x

def LU_solve(A, b):
    L, U = LU(A)
    y = Ly(L, b)
    x = Ux(U, y)
    return x
