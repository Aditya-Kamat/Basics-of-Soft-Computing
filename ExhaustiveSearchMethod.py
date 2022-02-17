# Minimize y = f(x) = 32/(x**2) + x, 0 <= x <= 10.0

# Create the objective function
def obj(x):
    y = 32/(x**2) + x
    return y

# Divide the given range into (n) smaller points between the minimum and maximum points
x_min = 0.1
x_max = 10.0
n = 10

# Iterations for Exhaustive Search Method

for i in range(10): # i is the number of times the search range is reduced
    x1 = x_min
    x3 = x1
    delta_x = (x_max - x_min)/n

    while x3 <= x_max: # The given range between x-min and x_max is searched for the minimum point
        x1 = x1
        x2 = x1 + delta_x
        x3 = x1 + 2*delta_x

        if obj(x1) > obj(x2) < obj(x3): # This condition defines the minimum point as between x1 and x3
            print("Minimum range is around ({}, {})".format(x1, x3))

            # Redefining the search range
            x_min = x1
            x_max = x3
            break
        
        x1 = x2

x_opt = (x1+x3)/2
y = obj(x_opt)

print("The minmum value of the given function is {}, at x = {}".format(y,x_opt))