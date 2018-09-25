# -*- coding: utf-8 -*-
"""Distribution of activation values for each layer
when randomly generated input data is spilled on a five-story neural network using the Sigmoid function
"""
import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.random.randn(1000, 100) # data
node_num = 100 # number of nodes per on each hidden layer
hidden_layer_size = 5
activations = {} # save activation values

for idx in range(hidden_layer_size):
    if idx != 0:
        x = activations[idx - 1]

    w = np.random.randn(node_num, node_num) / np.sqrt(node_num)
    a = np.dot(x, w)
    z = sigmoid(a)
    activations[idx] = z

# histogram
for key, value in activations.items():
    plt.subplot(1, len(activations), key+1)
    plt.title(str(key+1) + "-layer")
    plt.hist(value.flatten(), 30, range=(0,1))
plt.show()