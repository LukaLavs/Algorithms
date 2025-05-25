from math import factorial, sin
from matplotlib import pyplot as plt
from fractions import Fraction

def use_fractions(numbers):
    """ Converts list of numbers to Fraction class """
    return [Fraction(num) if not isinstance(num, Fraction) else num for num in numbers]

def sort_values(x_values, y_values):
    """ Sorts the points and prepares them for use """
    T = sorted(enumerate(x_values), key=lambda x: x[1])
    x_values, y_values = [x for (i, x) in T], [y_values[i] for (i, x) in T]
    return x_values, y_values

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
    
def F(x_values, f):
    """ vectorizes f function """
    return [f(x) for x in x_values]
    
def coefficients(x_values, y_values, fractions=False):
    """ Returns coefficients of Newton interpolation polinom """
    x_values, y_values = sort_values(x_values=x_values, y_values=y_values)
    if fractions: x_values, y_values = use_fractions(x_values), use_fractions(y_values)
    return [deljena_diferenca(D=x_values[0:i], x_values=x_values, y_values=y_values)
            for i in range(1, len(x_values) + 1)]  
     
def modified_horner(x, coefficients, x_values):
    """ Used for evaluating Newton interpolation polinom """
    v = x_values[-1]
    for i in range(2, len(x_values) + 1):
        v = coefficients[-i] + (x - x_values[-i]) * v
    return v
    
def Linspace(a, b, n):
    return [a + (b-a)*i/(n-1) for i in range(n)]  
    
def plot(x_values, y_values, A=1, B=1, f=None, y_min=None, y_max=None, fractions=False, smoothness=100):
    """
    Plots a given function with specified bleed amounts and axis limits.

    Parameters:
    A (float): The amount to bleed on the left side of the plot.
    B (float): The amount to bleed on the right side of the plot.
    f (function): The function to be plotted.
    y_min (float): The minimum value for the y-axis.
    y_max (float): The maximum value for the y-axis.
    fractions (bool, optional): If True, performs exact calculations using fractions. Default is False.
    smoothness (int, optional): The number of points to generate for a smoother curve. Default is 100.

    Returns:
    None
    """
    indexes = []
    x_prev = None
    for i in range(len(x_values)):
        x_current = x_values[i]
        if x_current == x_prev:
            indexes.append(i)
        x_prev = x_current
    X_points = [x_values[i] for i in range(len(x_values)) if not i in indexes]
    Y_points = [y_values[i] for i in range(len(y_values)) if not i in indexes]
    coef = coefficients(x_values=x_values, y_values=y_values, fractions=fractions)
    print("coefficients: ", [str(c) for c in coef])
    a, b = min(X_points), max(X_points)
    X = Linspace(a - A, b + B, smoothness*int(b - a + A + B))
    Y = [modified_horner(x, coef, x_values) for x in X]
    plt.figure(figsize=(8, 5))
    plt.plot(X, Y, label='p(x)', color='blue')
    if f: plt.plot(X, F(X, f), label='f(x)', color='black')
    plt.scatter(X_points, Y_points, color='red', label='Interpolation points')
    if y_min and y_max: plt.ylim(y_min, y_max)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Newton interpolation')
    plt.legend()
    plt.show()