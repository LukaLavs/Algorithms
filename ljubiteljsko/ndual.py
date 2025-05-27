import math

class NDualNumber:
    def __init__(self, coeffs, n=None):
        if n:
            # Then coeffs is a, point for derivate, construct Ndual[a, 1, 0, ..., 0]
            a = coeffs
            self.coeffs = list([a, 1] + [0] * n)
            self.n = n
        else:
            self.coeffs = list(coeffs)
            self.n = len(coeffs) - 1

    def __add__(self, other):
        if isinstance(other, NDualNumber):
            return NDualNumber([a + b for a, b in zip(self.coeffs, other.coeffs)])
        else:
            coeffs = self.coeffs[:]
            coeffs[0] += other
            return NDualNumber(coeffs)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, NDualNumber):
            return NDualNumber([a - b for a, b in zip(self.coeffs, other.coeffs)])
        else:
            coeffs = self.coeffs[:]
            coeffs[0] -= other
            return NDualNumber(coeffs)

    def __rsub__(self, other):
        return (-self) + other

    def __neg__(self):
        return NDualNumber([-a for a in self.coeffs])

    def __mul__(self, other):
        if isinstance(other, NDualNumber):
            n = self.n
            result = [0.0] * (n + 1)
            for i in range(n + 1):
                for j in range(n + 1 - i):
                    result[i + j] += self.coeffs[i] * other.coeffs[j]
            return NDualNumber(result)
        else:
            return NDualNumber([a * other for a in self.coeffs])

    def __rmul__(self, other):
        return self * other

    def __pow__(self, other):
        return pow(self, other)
    
    def __truediv__(self, other):
        if isinstance(other, NDualNumber):
            # Division via Newton method or recursive formula
            n = self.n
            a = self.coeffs
            b = other.coeffs
            q = [0.0] * (n + 1)
            q[0] = a[0] / b[0]
            for k in range(1, n + 1):
                s = a[k]
                for j in range(1, k + 1):
                    s -= b[j] * q[k - j] if j <= n and k - j <= n else 0.0
                q[k] = s / b[0]
            return NDualNumber(q)
        else:
            return NDualNumber([a / other for a in self.coeffs])

    def __rtruediv__(self, other):
        return NDualNumber([other]) / self

    def __repr__(self):
        return f"NDual({self.coeffs})"
    
    def derivate(self, m):
        n = self.n
        if m == "all":
            return [self.coeffs[k] * math.factorial(k) for k in range(0, n + 1)]
        if 0 <= m <= n:
            return self.coeffs[m] * math.factorial(m)





#################################


def evaluate_f(derivs, X):
    """Evaluate f(X), where X is an NDualNumber, using Taylor expansion."""
    n = X.n
    a = X.coeffs[0]
    B = NDualNumber([0.0] + X.coeffs[1:])

    result = NDualNumber([0.0] * (n + 1))
    B_power = NDualNumber([1.0] + [0.0] * n)  # B^0 = 1

    for k in range(n + 1):
        if derivs[k] == None:
            break
        term_coeff = derivs[k](a) / math.factorial(k)
        term = B_power * term_coeff
        result = result + term
        B_power = B_power * B  # B^k → B^{k+1}

    return result

def expirimental_pow(X, y):
    n = X.n
    derivs = [( lambda x, i=i: x**(y - i) * (math.gamma(y + 1) / math.gamma(y - i + 1)) ) if (y - i) >= 0 else None
              for i in range(0, n + 1)]
    return evaluate_f(derivs, X)

# --- Trigonometry ---

def sin(X):
    # X as a dual number
    n = X.n
    derivs = []
    sign = -1
    for k in range(0, n + 1):
        if k % 2 == 0:
            sign *= -1
            derivs.append(lambda x, s=sign: s * math.sin(x))
        else:
            derivs.append(lambda x, s=sign: s * math.cos(x))
    return evaluate_f(derivs, X)

def cos(X):
    n = X.n
    derivs = []
    sign = 1
    for k in range(n + 1):
        if k % 2 == 0:
            derivs.append(lambda x, s=sign: s * math.cos(x))
            sign *= -1
        else:
            derivs.append(lambda x, s=sign: s * math.sin(x))
    return evaluate_f(derivs, X)

def tan(X):
    return sin(X) / cos(X)

def cot(X):
    return cos(X) / sin(X)

# --- Preparation for trigonometric inverses ---

def pochhammer(x, k):
    return math.gamma(x + k) / math.gamma(x)

def hypergeometric_pfq_regularized(a_params, b_params, X, n_derivate):
    """
    Evaluate the regularized generalized hypergeometric function on dual number X.
    a_params, b_params: lists of floats (parameters)
    X: NDualNumber
    n: degree of expansion (should match X.n)
    """
    # Compute denominator Gamma product (constant)
    gamma_prod = 1.0
    for b in b_params:
        gamma_prod *= math.gamma(b)

    n = X.n
    result = NDualNumber([0.0] * (n + 1))
    X_power = NDualNumber([1.0] + [0.0] * n)  # X^0 = 1

    for k in range(n_derivate + 1):
        numerator = 1.0
        for a in a_params:
            numerator *= pochhammer(a, k)
        denominator = 1.0
        for b in b_params:
            denominator *= pochhammer(b, k)
        coeff = numerator / denominator / math.factorial(k) / gamma_prod
        term = X_power * coeff
        result = result + term
        X_power = X_power * X  # increment power z^{k+1}

    return result


# --- Inverses for trigonometric functions ---
# Requires calculations of 2^(-1 + n) Sqrt[\[Pi]] x^(1 - n)
#  HypergeometricPFQRegularized[{1/2, 1/2, 1}, {1 - n/2, (3 - n)/2}, x^2] function

# --- Hyperbolic functions ---

def cosh(X):
    return (exp(X) + exp(-X)) / 2

def sinh(X):
    return (exp(X) - exp(-X)) / 2

def tanh(X):
    return sinh(X) / cosh(X)

def coth(X):
    return cosh(X) / sinh(X)

# --- Inverse Hyperbolic Functions ---

def asinh(X):
    return log(X + sqrt(X*X + 1))

def acosh(X):
    if X.coeffs[0] >= 0:
        return log(X + sqrt(X*X - 1))
    print("Error in domain for acosh")
    return None

def atanh(X):
    if abs(X.coefss[0]) < 1:
        return 0.5 * log((1 + X) / (1 - X))
    print("Error in atanh domain")
    return None

def acoth(X):
    if abs(X.coeffs[0]) > 1:
        return 0.5 * log((1 - X) / (1 + X))
    print("Error in acoth domain")
    return None

# --- Exponential functions --- 

def exp(X):
    n = X.n
    derivs = [math.exp] * (n + 1)
    return evaluate_f(derivs, X)

def expm1(X):
    return exp(X) - 1
    
def sqrt(X):
    return pow(X, 0.5)

def comb(K, n):
    p = K
    for i in range(1, n):
        p *= (K - i)
    return p / math.factorial(n)

def factorial(X):
    a = X.coeffs[0]
    if isinstance(a, int):
        p = X
        for i in range(1, a):
            p *= (X - i)
        return p
    print("factorial not possible, perhaps you meant factorialpower")
    return None

def factorialpower(X, n):
    """returns X*(X - 1)*...*(X - n + 1)"""
    p = X
    for i in range(1, n):
        p *= (X - i)
    return p 

def pow(X, Y):
    """ Will give wrong results if derivates at 0 don't exist """
    a = X.coeffs[0]
    if a != 0:
        return exp(Y * log(X))
    if isinstance(Y, int):
        p = X
        for i in range(1, Y):
            p *= X
        return p
    if isinstance(Y, float):
        print("expirimental pow used, will not notify if result non existant")
        return expirimental_pow(X, Y)
    print("pow can't handle it yet")
    return None
# --- Logarithms ---

def log(X, base="e"):
    if base != "e" and base > 0 and base != 1:
        return log(X) / math.log(base)
    n = X.n
    derivs = [lambda x: math.log(x)] + [lambda x, s=(-1)**(k-1), f=math.factorial(k-1), k=k: s * f * x**(-k) for k in range(1, n+1)]
    return evaluate_f(derivs, X)

def log1p(X):
    return log(1 + X)

def log2(X):
    return log(X, 2)

def log10(X):
    return log(X, 10)




