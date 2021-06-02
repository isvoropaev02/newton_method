import numpy as np
import math

E = 0.0001
X = np.array([-1, -1])


def jacobian(v):
    return np.array([[-math.sin(v[0] + 0.5), -1], [-2, math.cos(v[1])]])


def system(v):
    s = np.array([math.cos(v[0] + 0.5) - v[1] - 2, math.sin(v[1]) - 2 * v[0] - 1])
    return s


def solution(v):
    jac_inv = np.linalg.inv(jacobian(v))
    s = system(v)
    xk = v
    xn = xk - np.matmul(jac_inv, s)
    while np.linalg.norm(xn - xk) >= E:
        xk = xn
        jac_inv = np.linalg.inv(jacobian(xk))
        s = system(xk)
        xn = xk - np.matmul(jac_inv, s)
    print(xn)


solution(X)
