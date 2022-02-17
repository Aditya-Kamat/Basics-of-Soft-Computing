import numpy as np
import sympy as sym

x, y, l = sym.symbols('x y l')

# Minimize f(x1,x2) = 4(x1**2) + x2**2 - 3x1*x2 + 6x1 + 12x2, -100.0 <= x1, x2 <= 100.0
def obj(x):
    exp = 4*(x[0]**2) + x[1]**2 - 3*x[0]*x[1] + 6*x[0] + 12*x[1]
    return exp

exp = 4*(x**2) + y**2 - 3*x*y + 6*x + 12*y

# Define initial variables
x1 = np.array([0.0, 0.0])
dell = [0, 0]
X1 = np.array([0,0])

dell[0] = sym.diff(exp, x) # partial diff of x
dell[1] = sym.diff(exp, y) # partial diff of y

X1[0] = dell[0].subs(x, x1[0]).subs(y, x1[1]) # substituing values into the partial diff
X1[1] = dell[1].subs(x, x1[0]).subs(y, x1[1])

for i in range(100):
    
    S = -1*X1

    X2 = x1 + l*S
    print(X2)

    f = obj(X2)
    f1 = sym.diff(f, l)

    l_opt = sym.solve(f1, l)
    print(l_opt)

    x2 = x1 + l_opt*S
    print(x2)

    X1[0] = dell[0].subs(x, x2[0]).subs(y, x2[1])
    X1[1] = dell[1].subs(x, x2[0]).subs(y, x2[1])

    print(X1)
    comp = X1 == np.array([0, 0])
    if comp.all():
        break
        
    else:
        x1 = x2

print(x2)
print(obj(x2))