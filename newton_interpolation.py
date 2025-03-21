from math import factorial

def last_index(x, lst):
    return len(lst) - lst[::-1].index(x) - 1

def k_th_derivate(x, k, x_values, y_values):
    """ Finds k-th derivate in y_values """
    index = x_values.index(x) + k
    return y_values[index]

def deljena_diferenca(D, x_values, y_values):
    """ Uses recursive algorithm for calculation of the coefficients """
    k = len(D)
    if k == 1:
        return y_values[x_values.index(D[0])]
    if all(x == D[0] for x in D):
        return k_th_derivate(D[0], k-1, x_values, y_values) / factorial(k-1)
    else:
        return ( deljena_diferenca(D[1:], x_values, y_values) - deljena_diferenca(D[:(k-1)], x_values, y_values) ) / (D[-1] - D[0])
    
def F(x_values):
    """ vectorizes f function """
    def f(x):
        return 4 / (1 + x)
    return [f(x) for x in x_values]
    
def coefficients(x_values, y_values):
    """ Returns coefficients of Newton interpolation polinom """
    return [deljena_diferenca(D=x_values[0:i], x_values=x_values, y_values=y_values)
            for i in range(1, len(x_values) + 1)]  
     
def modified_horner(x, coefficients, x_values):
    """ Used for evaluating Newton interpolation polinom """
    v = x_values[-1]
    for i in range(2, len(x_values) + 1):
        v = coefficients[-i] + (x - x_values[-i]) * v
    return v
    
    
##################### TEST ##############################
K = coefficients(x_values=[0, 0, 0, 1, 1, 1], y_values=[4, -4, 8, 2, -1, 1])
K = coefficients(x_values=[1, 2, 3, 4], y_values=[1, 2, 5, 3, 8])
x_values=[1, 2, 3, 4]
print(modified_horner(0, K, x_values))