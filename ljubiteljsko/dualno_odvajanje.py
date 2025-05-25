import math

class Dual:
    def __init__(self, real, dual):
        self.real = real
        self.dual = dual

    def __add__(self, other):
        if isinstance(other, Dual):
            return Dual(self.real + other.real, self.dual + other.dual)
        else:
            return Dual(self.real + other, self.dual)
    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, Dual):
            return Dual(self.real - other.real, self.dual - other.dual)
        else:
            return Dual(self.real - other, self.dual)
    def __rsub__(self, other):
        return Dual(other - self.real, -self.dual)

    def __mul__(self, other):
        if isinstance(other, Dual):
            return Dual(self.real * other.real,
                        self.real * other.dual + self.dual * other.real)
        else:
            return Dual(self.real * other, self.dual * other)
    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, Dual):
            a, b = self.real, self.dual
            c, d = other.real, other.dual
            return Dual(a / c, (b * c - a * d) / (c ** 2))
        else:
            return Dual(self.real / other, self.dual / other)
    def __rtruediv__(self, other):
        a, b = other, 0
        c, d = self.real, self.dual
        return Dual(a / c, (b * c - a * d) / (c ** 2))

    def __pow__(self, power):
        # Podpora za celo in realne eksponente (ne dualne)
        if isinstance(power, int):
            if power == 0:
                return Dual(1, 0)
            elif power > 0:
                result = Dual(self.real, self.dual)
                for _ in range(power - 1):
                    result = result * self
                return result
            else:
                return (Dual(1, 0) / (self ** abs(power)))
        elif isinstance(power, float) or isinstance(power, int):
            return dual_exp(Dual(power, 0) * dual_log(self))
        else:
            raise NotImplementedError("Potenciranje z ne-celim eksponentom ni podprto")

    def __repr__(self):
        return f"Dual(real={self.real}, dual={self.dual})"


# Eksponentne in logaritmične funkcije
def dual_exp(x):
    e = math.exp(x.real)
    return Dual(e, x.dual * e)

def dual_expm1(x):
    ex = math.exp(x.real)
    return Dual(ex - 1, x.dual * ex)

def dual_log(x):
    return Dual(math.log(x.real), x.dual / x.real)

def dual_log10(x):
    return Dual(math.log10(x.real), x.dual / (x.real * math.log(10)))

def dual_log1p(x):
    return Dual(math.log1p(x.real), x.dual / (1 + x.real))

def dual_log2(x):
    return Dual(math.log2(x.real), x.dual / (x.real * math.log(2)))

def dual_pow(x, y):
    # y je Dual ali float/int
    if isinstance(y, Dual):
        # Odvod za x^y z obema dualnima deloma je kompleksnejši,
        # tu pa implementiramo samo za y realno število (ali y.dual=0)
        if y.dual != 0:
            raise NotImplementedError("Potenciranje z dualnim eksponentom ni podprto.")
        y_real = y.real
    else:
        y_real = y
    return dual_exp(Dual(y_real, 0) * dual_log(x))

def dual_sqrt(x):
    sqrt_val = math.sqrt(x.real)
    return Dual(sqrt_val, x.dual / (2 * sqrt_val))


# Trigonometrične funkcije
def dual_sin(x):
    return Dual(math.sin(x.real), x.dual * math.cos(x.real))

def dual_cos(x):
    return Dual(math.cos(x.real), -x.dual * math.sin(x.real))

def dual_tan(x):
    tan_val = math.tan(x.real)
    return Dual(tan_val, x.dual / (math.cos(x.real) ** 2))

def dual_asin(x):
    return Dual(math.asin(x.real), x.dual / math.sqrt(1 - x.real ** 2))

def dual_acos(x):
    return Dual(math.acos(x.real), -x.dual / math.sqrt(1 - x.real ** 2))

def dual_atan(x):
    return Dual(math.atan(x.real), x.dual / (1 + x.real ** 2))

def dual_sinh(x):
    return Dual(math.sinh(x.real), x.dual * math.cosh(x.real))

def dual_cosh(x):
    return Dual(math.cosh(x.real), x.dual * math.sinh(x.real))

def dual_tanh(x):
    t = math.tanh(x.real)
    return Dual(t, x.dual * (1 - t**2))

def dual_asinh(x):
    return Dual(math.asinh(x.real), x.dual / math.sqrt(x.real**2 + 1))

def dual_acosh(x):
    return Dual(math.acosh(x.real), x.dual / math.sqrt(x.real**2 - 1))

def dual_atanh(x):
    return Dual(math.atanh(x.real), x.dual / (1 - x.real**2))


def dual_fabs(x):
    # Odvod abs je 1 ali -1, razen v 0, kjer ni definiran
    if x.real > 0:
        return Dual(abs(x.real), x.dual)
    elif x.real < 0:
        return Dual(abs(x.real), -x.dual)
    else:
        # Odvod ni definiran natanko v 0, tu vrnemo 0 kot približek
        return Dual(0.0, 0.0)

def dual_degrees(x):
    return Dual(math.degrees(x.real), x.dual * 180 / math.pi)

def dual_radians(x):
    return Dual(math.radians(x.real), x.dual * math.pi / 180)


################################################################
# --- Primer ---
# Želimo izračunati odvod za f; evaluiramo ga v točki Dual(x, 1); to vrne f(x) + 1*epsilon*f'(x);
# vrednost odvoda tako dobimo kot result.dual
# Za dualno število Dual(a, b) = a + b*epsilon velja: f(a + b*epsilon) = f(a) + b*f'(a)*epsilon = Dual(f(a), b*f'(a))

def f(x):
    # f(x) = sin(x) * exp(cos(x)) + log(x^2 + 2) * tanh(x)
    return math.sin(x)*math.exp(math.cos(x)) + math.log(x**2 + 2)*math.tanh(x)

def complex_function(x):
    # f(x) = sin(x) * exp(cos(x)) + log(x^2 + 2) * tanh(x)
    term1 = dual_sin(x) * dual_exp(dual_cos(x))
    x_squared_plus_one = x * x + Dual(2, 0)
    term2 = dual_log(x_squared_plus_one) * dual_tanh(x)
    return term1 + term2

# Test na x = 1.0
x = Dual(1.0, 1.0)  # dual=1 za odvod po x

result = complex_function(x)
h = 1e-10; result_aprox = (f(1+h) - f(1))/h
print(f"f({x.real}) = {result.real}")
print(f"f'({x.real}) = {result.dual}")
print(f"f'_aprox({x.real}) = {result_aprox}")
