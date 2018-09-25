# -*- coding: utf-8 -*-
import numpy as np


def cross_entropy_errpr(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))
"""np.log가 0이 되면 마이너스 무한대를 뜻하는 -inf가 되어 더 이상 계산을 진행할 수 없다
따라서 아주 작은 값 delta를 더해 np.log값이 0이 되지 않게 한다
"""