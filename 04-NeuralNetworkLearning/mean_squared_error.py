# -*- coding: utf-8 -*-
import numpy as np


def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)
"""y는 각 원소의 출력(추정값)
t는 정답 레이블(실제값)
"""