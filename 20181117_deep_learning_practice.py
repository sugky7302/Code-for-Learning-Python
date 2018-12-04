import numpy as np

class NeuralNetwork:
    def __init__(self, X, Y, layerDim, studyingIteration = 2000, learningRate):
    """
    Implements a L-layer neural network: [LINEAR->RELU]*(L-1)->LINEAR->SIGMOID.
    
    Arguments:
    X -- data, numpy array of shape (number of examples, num_px * num_px * 3)
    Y -- true "label" vector (containing 0 if cat, 1 if non-cat), of shape (1, number of examples)
    layersDim -- list containing the input size and each layer size, of length (number of layers + 1).
    learningRate -- learning rate of the gradient descent update rule
    studyingIteration -- number of iterations of the optimization loop
    """
        parameters = _InitParameters(layerDim)
        L = len(parameters) // 2
        for i in range(0, studyingIteration):
            AL, caches = _Forward(X, parameters, L)
            cost = ComputeCost(AL, Y)
            grads = _Backward(AL, Y, parameters, caches)
            _UpdateParameters(parameters, grads, learningRate)

    def _InitParameters(layerDim):
        parameters = {}
        L = len(layerDim)
        np.random.seed(3)
        for i in Range(1, L):
            parameters['W' + str(i)] = np.random.randn(layerDim[i], layerDim[i-1]) * 0.01
            parameters['b' + str(i)] = np.zeros(layerDim[i], 1)

        return parameters

    def _Forward(X, parameters, deeper):
        caches = []
        A = X
        for i in Range(1, deeper):
            Z = np.dot(parameters['W' + str(i)], A) + parameters['b' + str(i)]
            A = ReLU(Z)
            caches.append((Z, A))

        ZL = np.dot(parameters['W' + str(deeper)], A) + parameters['b' + str(deeper)]
        AL = Sigmoid(ZL)
        caches.apend((ZL, AL))

        return AL, caches

    def ReLU(Z):
        result = np.maximum(0, Z)
        return result

    def Sigmoid(Z):
        result = 1 / (1 + np.exp(-Z))
        return result
        
    def ComputeCost(AL, Y):
        m = Y.shape[1]
        result = -np.sum(np.dot(Y, np.log(AL).T) + np.dot(1 - Y, np.log(1 - AL).T), axis = 1, keepdims = True) / m
        return result

    def _Backward(AL, Y, parameters, caches):
        grads = {}
        L = len(caches)
        m = AL.shape[1]
        Y = Y.reshape(AL.shape)
        
        dAL = -(np.divide(Y, AL) - np.divide(1 - Y, 1 - AL))
        dZL = Derivate_sigmoid(dAL)
        A = caches[L - 1][1]
        grads["dW" + str(L)] = np.dot(dZL, A.T) / m
        grads["db" + str(L)] = np.sum(dZL, axis = 1, keepdims = True) / m
        grads["dA" + str(L-1)] = np.dot(parameters['W' + str(L)], dZL)
    
        # Loop from l=L-2 to l=0
        for l in reversed(range(L-1)):
            A = caches[l][1]
            dZ = Derivate_relu(grads['dA' + str(l + 1)])
            grads["dA" + str(l)] = np.dot(parameters['W' + str(l)], dZ)
            grads["dW" + str(l + 1)] = np.dot(dZ, A.T) / m
            grads["db" + str(l + 1)] = np.sum(dZ, axis = 1, keepdims = True) / m

        return grads

    def = _UpdateParameters(parameters, grads, learningRate):
        L = len(parameters) // 2
        for i in Range(1, L):
            parameters['W' + str(i)] = parameters['W' + str(i)] - learningRate * grads['dW' + str(i)]
            parameters['b' + str(i)] = parameters['b' + str(i)] - learningRate * grads['db' + str(i)]
