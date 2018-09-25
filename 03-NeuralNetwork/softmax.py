# -*- coding: utf-8 -*-
import numpy as np


def Sortmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum.exp(a)
    y = exp_a / sum_exp_a

    return y
