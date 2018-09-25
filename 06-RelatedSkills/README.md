# Parameter renewal
The purpose of neural network learning is to find parameters  
that reduce the value of a lost function as much as possible.  
This is the question of finding the best value for the parameter, which is called optimization.
* SGD(Stochastic Gradient Descent)  
* Momentum  
* AdaGrad  
* Adam

There is always no an excellent technique for every problem.  
Let's try various things considering the situation.

# Initial value of weight
Weight decay is a technique that increases general-purpose performance by suppressing overfitting.  
Setting the weights to a uniform value eliminates the meaning of having multiple weights,  
since they remain the same after renewal.  
Therefore, the initial value should be set at random.
* Xavier
* He

# Batch Normalization
It forces each layer to spread the activation moderately.  
Batch normalization reduces the need to worry about learning speed,  
overfitting and setting inital value.
