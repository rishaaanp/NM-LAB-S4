def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1

def newton_raphson(x0, tol, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)

        if dfx == 0:
            print("Derivative is zero. Method fails.")
            return None

        x_new = x - fx / dfx

        if abs(x_new - x) < tol:
            return x_new  

        x = x_new

    print("Method did not converge.")
    return None

# Example 
initial_guess = 1.5
tolerance = 0.0001

root = newton_raphson(initial_guess, tolerance)
print("Root:", root)
