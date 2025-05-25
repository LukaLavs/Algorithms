def find_increasing_path(S, T, M, connections):
    # Poišči prosto vozlišče v T:
    for v in T:
        if all(((u, v) not in M) for u in S):   
            # Poišči s čim v S je v povezan
            for (u, v_candidate) in connections:
                if v_candidate == v and u in S:                   
                    path = [(u, v)]
                    route = "in_M"
                    while True:                      
                        if route == "in_M":
                            # Pomeni da smo v X delu grafa
                            u = path[-1][0]
                            # Poišči povezavo po M
                            for (u_candidate, v) in M:
                                if u_candidate == u:
                                    path.append((u, v))
                                    route = "not_in_M"
                                    break
                            else: break
                        else:
                            # Smo v Y delu grafa
                            v = path[-1][1]
                            # Poisšči povezavo izven M
                            for (u, v_candidate) in connections:
                                if (u, v_candidate) not in M and v_candidate == v:
                                    path.append((u, v))
                                    route = "in_M"
                                    break
                            else: break
                    return path         
    return None


def solve_graph(M):

    X, Y = list(range(len(M))), list(range(len(M[0])))
    connections = [(row, col) for row in range(len(M)) for col in range(len(M[0])) if M[row][col] == 0]
    M = set()  
    S, T = set(u for u in X if not any((u, v) in M for v in Y)), set()

    while True:    
        S, T = set(u for u in X if not any((u, v) in M for v in Y)), set()
        S_prev, T_prev = None, None       
        # Dokler nista S in T enaka starima:
        while S != S_prev or T != T_prev:
            S_prev, T_prev = S, T 
            T = T | {v for v in Y if any(((u, v) in connections and (u, v) not in M) for u in S)}
            S = S | {u for u in X if any(((u, v) in M) for v in T)}
            # Če v T ni prostega vozlišča, smo našli povečujočo pot:
            if any((v not in [m[1] for m in M]) for v in T):
                break

        path = find_increasing_path(S, T, M, connections)
        # Če ni povečujoče poti smo končali:
        if path == None: return (M, S, T)
        # Povečajmo prirejanje:
        for i, pair in enumerate(path):
            if i % 2 == 0:
                M.add(pair)
            else:
                M.discard(pair)   


def hungarian_method(M, show_steps=False):
    if show_steps:
        print("Original")  
        for i in M:
            print(i)
        print("\n")  
    # Odštej minimalni element za vsako vrstico
    for row in range(len(M)):
        minimal = min(M[row])
        for i in range(len(M[row])):
            M[row][i] -= minimal
    if show_steps:
        print("Rows")  
        for i in M:
            print(i)
        print("\n")        
    # Odštej minimalni element za vsak stolpec
    for col in range(len(M[0])):
        minimal = min([M[j][col] for j in range(len(M))])
        for j in range(len(M)):
            M[j][col] -= minimal
    if show_steps: 
        print("Cols") 
        for i in M:
            print(i)
        print("\n")        
    while True:        
        # Ustvarimo dvodelni graf z povezavami tam kjer so ničle, in poiščemo največje prirejanje:   
        (matching, S, T) = solve_graph(M) 
        if len(matching) == len(M): return matching
        # Poiščemo min od nepokritih elementov
        rows, colls = [i for i in range(len(M)) if i not in S], list(T)
        not_covered = []
        for row in range(len(M)):
            for col in range(len(M[0])):
                if row not in rows and col not in colls:
                    not_covered.append(M[row][col])
        minimal = min(not_covered)
        # Odštejemo min nepokritih od stolpcev iz T in vrstic, ki niso v S:
        for row in range(len(M)):
            for col in range(len(M[0])):
                if row in rows:
                    if col in colls:
                        M[row][col] += minimal
                    continue
                if row not in rows and col not in colls:
                    M[row][col] -= minimal
        if show_steps: 
            print("Matching") 
            for i in M:
                print(i)
            print("\n")


def matrix_sum(Matrix, way="min", show_steps=False):
    if way == "min":
         M = [[Matrix[i][j] for j in range(len(Matrix[0]))] for i in range(len(Matrix))]
    if way == "max":
        M = [[-Matrix[i][j] for j in range(len(Matrix[0]))] for i in range(len(Matrix))]
    if way == "max_product":
        import math
        M = [[-math.log10(Matrix[i][j]) for j in range(len(Matrix[0]))] for i in range(len(Matrix))]
    if way == "min_product":
        import math
        M = [[math.log10(Matrix[i][j]) for j in range(len(Matrix[0]))] for i in range(len(Matrix))]
    if way == "min" or way == "max":    
        permutation = hungarian_method(M, show_steps)
        print(f"positions: {sorted(permutation)}")
        result = 0
        for (i, j) in permutation:
            result += Matrix[i][j]
        return f"{way} sum: {result}"
    else:
        permutation = hungarian_method(M, show_steps)
        print(f"positions: {sorted(permutation)}")
        result = 1
        for (i, j) in permutation:
            result *= Matrix[i][j]
        return f"{way}: {result}"