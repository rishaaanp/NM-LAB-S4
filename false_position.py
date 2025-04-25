def f(x):
    return x**3 - x - 2

def false_position(a, b, tol):
    if f(a) * f(b) >= 0:
        print("False Position method fails. f(a) and f(b) must have opposite signs.")
        return None

    c = a  
    while True:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        
        if abs(f(c)) < tol:
            break 

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return c

# Example 
a = 1
b = 2
tolerance = 0.0001

root = false_position(a, b, tolerance)
print("Root:", root)
