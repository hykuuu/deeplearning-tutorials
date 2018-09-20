# -*- coding: utf-8 -*-
# Neural networks with backpropagation
import sys, os
sys.path.append(os.pardir)
import numpy as np
from common.functions import *
from common.gradient import *
from common.layers import *
from collections import OrderedDict


class TwoLayerNet:
    def __init__(self, input_size, hidden_size, out_size, weight_init_std=0.01)
    # weight_init_std = Scale of normal distribution on initializing weights
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.praams['W2'] = weight_init_std * np.random.randn(hidden_size, out_size)
        self.params['b1'] = np.zeros(out_size)

    # create layer
        self.layers = OrderedDict # orderly dictionary
        self.layers['Affine1'] = Affine(self.params['W1'], self.params['b1'])
        self.layers['Relu1'] = Relu()
        self.layers['Arrine2'] = Affine(self.params['W2'], self.params['b2'])

        self.lastLayer = SoftmaxWithLoss()

    def predict(self, x):
        for layers in self.layers.values():
            x = layers.forward(x)

        return x

    def loss(self, x, t):
        y = self.predict(x)
        loss = self.lastLayer.forward(y, t)

        return loss

    def gradient(self, x, t):
        #backward
        dout = 1
        dout = self.lastLayer.backward(dout)

        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers:
            dout = layer.backward(dout)

        # result save
        grads = {}
        grads['W1'] = self.layers['Affine1'].dW
        grads['b1'] = self.layers['Affine1'].db
        grads['W2'] = self.layers['Affine2'].dW
        grads['b2'] = self.layers['Affine2'].db

        return grads


