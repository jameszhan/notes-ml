# -*- coding:utf-8 -*-

from sigmoid import sigmoid
import numpy as np

def computeCost_reg(theta,X,y,lambd):
    m,n = X.shape
    h = sigmoid(np.dot(X,theta))
    theta_reg = np.concatenate((np.zeros((1,1)),theta[1:n,:]),axis=0)
    J = (np.dot(-y.T,np.log(h))-np.dot((1-y).T,np.log(1-h)))/m + lambd/(2*m)*sum(theta_reg**2)
    return J