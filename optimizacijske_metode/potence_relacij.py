def Relation(R, n):
    """ izračuna R^n, kjer je R relacija oblike {(a,b), ...}
    primer R = {(1, 2), (2, 3)} ali R = {("a", "b"), ("b", "c")} """
    # A je tak, da R ⊆ A × A, | je operator unije
    A = set(i for (i, j) in R) | set(j for (i, j) in R)
    # Im_R je slika relacije R
    Im_R = set(y for (x, y) in R)
    K = R # Inicializacija pred začetkom zanke
    for i in range(n-1): # i = 0,...,(n-2)
        K = {(x, z) for x in A for z in A if any((x, y) in R and (y, z) in K for y in Im_R)}
        # zdaj je K = R^(i+2); po definiciji kompozituma K <- K ° R
    return K
   
