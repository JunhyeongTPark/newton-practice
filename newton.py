def fx(x):
    '''
    The objective function.

    Inputs:
        x: the value for which the function is evaluated at (float)

    Outputs:
        Returns the function value evaluated at x.
    '''
    # return x**2
    return ((x**4)/4) - (x**3) - x

def derivative(x, fun, eps=1e-5):
    '''
    Returns the derivative of the objective function.

    Inputs:
        x:   the value for which the derivative is evaluated at (float)
        fun: the function for which the derivative is calculated (func)
        eps: small value for derivative evaluation (float)

    Outputs:
        Returns the derivative value evaluated at x.
    '''
    return (fun(x+eps) - fun(x)) / eps

def s_derivative(x, fun, eps=1e-3):
    '''
    Returns the second derivative of the objective function.

    Inputs:
        x:   the value for which the second derivative is evaluated at (float)
        fun: the function for which the second derivative is calculated (func)
        eps: small value for second derivative evaluation (float)

    Outputs:
        Returns the second derivative value evaluated at x.
    '''
    return (derivative(x+eps, fun) - derivative(x, fun)) / eps

def optimize(x0, fun, max_iters=50, tol=1e-6):
    '''
    Finds the minimum of a given objective function

    Inputs:
        x0:        the starting value for minimization (float)
        fun:       the function for which the minimum is calculated (func)
        max_iters: maximum number of iterations to avoid infinite looping (int)
        eps:       small value for derivation calculations (float)

    Outputs:
        Returns the second derivative value evaluated at x.
    '''
    x_prev = x0
    for i in range(max_iters):
        g = derivative(x_prev, fun)
        h = s_derivative(x_prev, fun)
        x = x_prev - g/h
        if x > 1e5:
           raise RuntimeError(f"At iteration {i}, optimization appears to be diverging")

        if abs(x - x_prev) < tol:
            break

        x_prev = x

    return x