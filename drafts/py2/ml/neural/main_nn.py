# -*-coding:utf-8 -*-
import scipy.io
import numpy as np
from predict_nn import predict_nn

data = scipy.io.loadmat('ex3data1.mat')
weights = scipy.io.loadmat('ex3weights.mat')
print '数据列有：',data.keys()
print '数据列有：',weights.keys()
# 所有像素点X
X = data['X']
y = data['y']
Theta1 = weights['Theta1']
Theta2 = weights['Theta2']

input_layer = 400
hidden_layer = 25
output_layer = 10


pred = predict_nn(Theta1,Theta2,X)
accuracy = np.mean(pred == y)
print 'Train accuracy is :%f\n' % accuracy