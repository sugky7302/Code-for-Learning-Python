import sys, os
sys.path.append(os.pardir)
from ref.dataset.mnist import load_mnist
import numpy as np
from PIL import Image

(x_train, t_train), (x_test, t_test) = load_mnist(flatten = True, normalize = False)

def StepFunction(x):
    return np.array(x > 0, dtype=np.int)

def Sigmoid(x):
    return 1 / (1 + np.exp(-x))

def ReLU(x):
    return np.maximum(0, x)

def SoftMax(x):
    fixValue = np.max(x)
    x -= fixValue
    exp_x = np.exp(x)
    sumExp_x = np.sum(exp_x)
    y = exp_x / sumExp_x
    return y

def InitNetwork():
    network = {}
    network['weight1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['bias1'] = np.array([0.1, 0.2, 0.3])
    network['weight2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['bias2'] = np.array([0.1, 0.2])
    network['weight3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['bias3'] = np.array([0.1, 0.2])
    return network

def IdentityFunc(x):
    return x

def forwardByIdentity(network, x, layer = 1):
    weight = network['weight' + str(layer)]
    bias = network['bias' + str(layer)]
    a = np.dot(x, weight) + bias
    if layer == 3 :
        y = IdentityFunc(a)
        return y
    else :
        layer += 1
        s = Sigmoid(a)
        return forwardByIdentity(network, s, layer)

def forwardBySoftMax(network, x, layer = 1):
    weight = network['weight' + str(layer)]
    bias = network['bias' + str(layer)]
    a = np.dot(x, weight) + bias
    if layer == 3 :
        y = SoftMax(a) 
        return y
    else :
        layer += 1
        s = Sigmoid(a)
        return forwardBySoftMax(network, s, layer)

def ImgShow(img):
    pilImg = Image.fromarray(np.uint8(img))
    pilImg.show()


# network = InitNetwork()
# x = np.array([1.0, 0.5])
# y = forwardByIdentity(network, x)
# print(y)
# y = forwardBySoftMax(network, x)
# print(y)
# print(x_train.shape)
# print(t_train.shape)
# print(x_test.shape)
# print(t_test.shape)
img = x_train[0]
label = t_train[0]
print(label)
print(img.shape)
img = img.reshape(28, 28)
print(img.shape)
ImgShow(img)