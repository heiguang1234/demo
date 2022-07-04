# 开发者：Hei guang
# 开发时间：2022/6/23 17:05


import numpy as np


def sigmoid(z):
    return 1/(1+np.exp(-z))



print(sigmoid(0))