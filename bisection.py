def f(x):
    return x**3 - x - 2

def bisection(a, b, tol):
    if f(a) * f(b) >= 0:
        print("Bisection method fails. f(a) and f(b) must have opposite signs.")
        return None

    while (b - a) / 2 > tol:
        c = (a + b) / 2 
        if f(c) == 0:
            return c  
        elif f(a) * f(c) < 0:
            b = c  
        else:
            a = c  
    
    return (a + b) / 2 

# Example
a = 1
b = 5
tolerance = 0.0001

root = bisection(a, b, tolerance)
print("Root:", root)
