import ndual
from ndual import NDualNumber

a = 0 # Točka odvajanja

X = NDualNumber([a, 1.0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0])  # Degree 9 dual number centered at a = 0
# The following is equivalent:
X = NDualNumber(a, n=9)

result = ndual.pow(X**2 + 1, 3.3) + ndual.sin(X)**2 + ndual.exp(-X**2) * ndual.cos(X)**3 + (X**2 + 1)**3.3

mathematica_result_8derivate = 51106.935999999994
our_result_8derivate = result.derivate(8)
print(f"napaka: {abs(mathematica_result_8derivate - our_result_8derivate)}")

print("[f(a), f'(a), f''(a), ...] = ", result.derivate("all"))
# ALgoritem da visoko natančnost, tu je napaka: 7.275957614183426e-11


