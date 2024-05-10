#前向传播神经元的实现
#p14

import numpy as np  #导入numpy模块，并重新命名为np
import math         #导入math模块

class Neuron(object):   #表示定义了一个名为 Neuron 的类，该类继承自 object 类
                        #object类是python中默认的类 不懂有啥用
    def __init__(self): #定义一个类的构造函数的方法
        self.weights = np.array([1.0,2.0]) #创建一个名为 weights 的实例属性，
                                           #并将其初始化为一个包含两个浮点数（1.0 和 2.0）的NumPy数组。
        self.biases = 0.0                  #创建一个名为 biases 的实例属性，并将其初始化为浮点数 0.0。
    def forward(self, inputs):
        """Assuming that inputs and weights are 1-D numpy arrays and the bias is a number"""
        a_cell_sum = np.sum(inputs * self.weights)+self.biases
        result = 1.0/(1.0 +math.exp(-a_cell_sum)) #这是sigmoid激活函数
        return result
neuron = Neuron()
output = neuron.forward(np.array([1,1]))
print (output)

