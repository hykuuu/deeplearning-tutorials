# -*- coding: utf-8 -*-


def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h)-f(x-h)) / (2*h)
"""수치미분: 아주 작은 차분으로 미분하는 것
근사치로 계산하는 방법"""