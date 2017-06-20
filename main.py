from __future__ import division
from loader import load
from sklearn import svm
import pandas as pd
import numpy as np
import scipy as scip
from scipy import linalg
from scipy.spatial.distance import pdist, squareform

beta1 = 2.0
beta2 = 1.0

# Support Vector Machine Hyperparameters
sigma = 1.0
length = 1.0 

sigma1 = 1.0
length1 = 1.0

sigma2 = 1.0
length2 = 1.0

noise = 0.00001

# RBF Kernal Function 
def K(x, sigma, length):
    return (sigma ** 2)*scip.exp(-(x ** 2) / (2 * length ** 2))

def dK_sigma(x, sigma, length):
    return (2*sigma)*scip.exp(- (x ** 2) / (2*length ** 2))

def dK_length(x, sigma, length):
    return ((x ** 2)/ (length ** 3))*(sigma ** 2)*scip.exp(- (x ** 2) / (2 *length ** 2))

def dL_dK(k_inv,y):
    return 0.5*(np.dot(np.dot(np.dot(k_inv,y),y.T),k_inv) - k_inv)

def dL_dtheta(k_inv, d_my_kernel, y_train):
    return 0.5*np.trace(np.dot(k_inv,d_my_kernel)) - 0.5*np.dot(np.dot(np.dot(np.dot(y_train.T,k_inv),d_my_kernel),k_inv),y_train)

# Accuracy function
def accuracy(error):
    num = 0
    for item in error:
        if item == 0:
            num = num + 1
    return (num/len(error))*100

# Data Preparation
data = load()
np.random.shuffle(data)
data = pd.DataFrame(data)
y1_train = data[data.columns[1]]
y2_train = data[data.columns[14]]
data = data.drop(data.columns[[1,2,14]], axis=1)
x_train = data
x_train = np.array(x_train.as_matrix(), dtype=np.float64)
y1_train = np.array(y1_train.values, dtype=np.float64)
y2_train = np.array(y2_train.values, dtype=np.float64)
print x_train
print y1_train
print y2_train

# Multi-Task Kernel 
pairwise_dists = squareform(pdist(x_train, 'euclidean'))
kernel = K(pairwise_dists,sigma,length)
kern_prod = np.kron(kernel, np.array([[beta1],[beta2]]))
k1 = kern_prod[:int(len(kern_prod)/2),:]
k2 = kern_prod[int(len(kern_prod)/2):,:]

# Kernel Error
k1_inv  = np.linalg.inv(k1 + noise*np.identity(len(k1)))
k2_inv  = np.linalg.inv(k2 + noise*np.identity(len(k2)))

k1_sigma_er = dL_dtheta(k1_inv, dK_sigma(k1,sigma1,length1), y1_train)
k2_sigma_er = dL_dtheta(k2_inv, dK_sigma(k2,sigma2,length2), y2_train)

k1_length_er = dL_dtheta(k1_inv, dK_length(k1,sigma1,length1), y1_train)
k2_length_er = dL_dtheta(k2_inv, dK_length(k2,sigma1,length1), y2_train)

sigma1 = sigma1 - k1_sigma_er
length1 = length1 - k1_length_er

sigma2 = sigma2 - k2_sigma_er
length2 = length2 - k2_length_er

k1_error = dL_dK(k1_inv, y1_train)
k2_error = dL_dK(k2_inv, y2_train)

k_error = beta1*k1_error + beta2*k2_error

# Optimize Betas
beta1 = beta1 - np.trace(k1_error)
beta2 = beta2 - np.trace(k2_error)

# Optimize K kernal
kernel_inv = np.linalg.inv(kernel + noise*np.identity(len(kernel)))
kernel_sigma_er = np.trace(np.dot(k_error, dK_sigma(kernel,sigma,length)))
kernel_length_er = np.trace(np.dot(k_error, dK_length(kernel,sigma,length)))

sigma = sigma - kernel_sigma_er 
length = length - kernel_length_er

print 'Done'


