def fx(x):
    return x**2

def derivative(x, fun, eps=1e-5):
    return (fun(x+eps) - fun(x)) / eps

def s_derivative(x, fun, eps=1e-5):
    return (derivative(x+eps, fun) - derivative(x, fun)) / eps

def optimize(x0, fun, max_iters=20, eps=1e-5):
    x_prev = x0
    for i in range(max_iters):
        g = derivative(x_prev, fun)
        h = s_derivative(x_prev, fun)
        x = x_prev - g/h

        if abs(x - x_prev) < eps:
            break


    return x

print(optimize(3, fx))

import numpy as np

print(optimize(2, np.cos))