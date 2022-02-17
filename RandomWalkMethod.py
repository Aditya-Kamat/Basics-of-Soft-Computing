import numpy as np

# Minimize f(x1,x2) = 4(x1**2) + x2**2 - 3x1*x2 + 6x1 + 12x2, -100.0 <= x1, x2 <= 100.0
def obj(x):
    y = 4*(x[0]**2) + x[1]**2 - 3*x[0]*x[1] + 6*x[0] + 12*x[1]
    return y

# Define initial variables
x = np.array([0.0, 0.0])
lmd = 1.0
eta = 0.25
N = 50

while lmd > eta: # Repeating until step length is less than minimum step length

    for i in range(N): # Performing optimization over maximum number of iterations (N)
        r = np.random.uniform(-1.0, 1.0, len(x)) # Generation of random array (r)
        b = 0

        for a in r:
            b = b+a**2

        u = (1/(b)) * r
        x_new = x + lmd*u # Creation of new solution

        if obj(x_new) < obj(x):
            x = x_new
        
    lmd = lmd*0.5 # Updating step length

print("Optimized value is {} at {}".format(obj(x), x))