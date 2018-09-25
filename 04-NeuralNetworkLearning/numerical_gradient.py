# -*- coding: utf-8 -*-
""""numerical gradient = 모든 변수의 편미분을 벡터로 정리한 것
배열 x의 각 원소에 대해서 수치 미분을 구함
"""
import numpy as np


def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x) # x와 형상이 같고 원소가 모두 0인 배열

    for idx in range(x.size):
        tmp_val = x[idx]

        # f(x+h)
        x[idx] = tmp_val + h
        fxh1 = f(x)

        # f(x-h)
        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val # 값 복원

    return grad
