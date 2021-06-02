import math

x = 1
a = -0.8
b = 1.2
h = 0.005
E = 0.0001
roots = []
r_bounds = []


def f(p_x):  # function
    g = p_x ** 2 - math.asin(p_x - 0.2)  # x \in [-0.8 ; 1.2]
    return g


def df_dx(p_x):  # derivative
    g1 = 2 * p_x - 5 / (math.sqrt(24 + 10 * p_x - 25 * (p_x ** 2)))
    return g1


def lock():
    p_x = a
    while p_x <= b:
        f1 = f(p_x)
        if p_x + h <= b:
            p_x = p_x + h
            f2 = f(p_x)
        else:
            break
        while f1 * f2 > 0:
            if p_x + h <= b:
                p_x = p_x + h
                f1 = f2
                f2 = f(p_x)
            else:
                break
        if p_x + h <= b:
            global r_bounds
            r_bounds.append([p_x - h, p_x])


def find_roots():
    for i in range(0, len(r_bounds)):
        xk = r_bounds[i][0]
        xn = xk - f(xk) / df_dx(xk)
        while abs(xn - xk) >= E:
            xk = xn
            xn = xk - f(xk) / df_dx(xk)
        global roots
        roots.append(xn)


def find_answer():
    ans = 0
    for i in range(0, len(roots)):
        if i == 0 and roots[i] != 0:
            ans = roots[i]
        elif abs(roots[i]) < abs(ans) and roots[i] != 0:
            ans = roots[i]
    if ans == 0:
        print('no roots or only 0 roots')
    else:
        print(ans)


lock()
find_roots()
print(roots)
find_answer()
