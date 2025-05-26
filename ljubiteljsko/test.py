


#funkcija = 2**(n_derivate-1) * math.pi**0.5 * pow(X, 1 - n_derivate) * hypergeometric_pfq_regularized(a_params, b_params, X*X, n_derivate)
#print(funkcija.derivate("all"))



#funkcija = 2**(n_derivate-1) * math.pi**0.5 * pow(X, 1 - n_derivate) * hypergeometric_pfq_regularized(a_params, b_params, X*X, n_derivate)

import ndual
from ndual import NDualNumber

def complex_function(x):
    return (
        ndual.exp(x * x) * ndual.sin(ndual.sqrt(x + 1)) +
        ndual.log(x * x + 2) * ndual.cos(X*X*X) +
        x * ndual.tan(x + 0.5)
    )
    
a = 0
X = NDualNumber([a, 1.0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0])  # Degree 4 dual number centered at x = 0
result = complex_function(X)
print(result.derivate("all"))  # Gives f(a), f'(a), ...
# ALgoritem da visoko natančnost
#opomba: dual.pow(X, Y) ne deluje če X[0] === 0

