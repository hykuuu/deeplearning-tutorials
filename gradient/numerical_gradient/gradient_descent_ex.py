# -*- coding: utf-8 -*-
# 경사법으로 f(x0, x1) = x0^2 + x1^2 최솟값 구하기
import numpy as np


def function(x):
    return x[0]**2 + x[1]**2


# 기울기 구하기
def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)

    for idx in range(x.size):
        tmp_val = x[idx]
        # f(x+h)
        x[idx] = tmp_val + h
        fxh1 = f(x)

        # f(x-h)
        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val

    return grad


# 경사하강법
def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x

    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad
    return x


# ex적용
init_x = np.array([-3.0, 4.0])
print(gradient_descent(function, init_x=init_x, lr=0.1, step_num=100))