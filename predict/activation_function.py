# -*- coding: utf-8 -*-
"""Activation function.

A function that converts the sum of the input signal to the output signal.
Role to determine if sum of input signals is active.
Use to convert data into nonlinearity.

The activation function of the output layer is set according to
the nature of the problem you are trying to solve.

common:
    regression: identity function.
    2class classification: sigmoid function.
    multi classification: softmax function.
"""
import numpy as np


def identity_function(x):
    return x


def step_function(x):
    return np.array(x > 0, dtype=np.int)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    return np.maximum(0, x)


def softmax(x):
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T

    x = x - np.max(x)  # Overflow countermeasure
    return np.exp(x) / np.sum(np.exp(x))