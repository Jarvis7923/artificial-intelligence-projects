"""
Main implementaion of the back propagation algorithm for ANN classification problem

author: shang wang
id: 1277417
email: swang27@tufts.edu

"""

# from numba import jit
import numpy as np
import time

from src.loginfo import show_loginfo, log_type


def run(tr_set, te_set, va_set, layers, alpha, iter):
    """
    train the ANN.

    Arguments:
        tr_set, te_set, va_set: indicating training set, testing set and validation set respectively
        layers: a list of number of nodes in the hidden layer
        alpha: momentum
        iter: maximum learning iteration
    """
    start = time.time()
    network = init_network(tr_set[0], tr_set[1], layers)

    # decode the onehot label for calculating the accuracy
    y_ = np.argmax(tr_set[1], axis=1)
    show_loginfo(log_type.info, "Maximum iterations: \n\t\t{0:d}".format(iter))
    show_loginfo(log_type.system, "Training ... ")
    for i in range(iter):
        network, out = back_prop_learning(tr_set[0], tr_set[1], alpha, network)
        acc = accuracy(np.argmax(out, axis=1), y_)
        show_loginfo(
            log_type.info, "accuracy on TRAINING set: {:.2f} %".format(100*acc), end='\r')
        if acc == 1.0:
            break
    show_loginfo(log_type.info, "accuracy on TRAINING set: {:.2f} %".format(100*acc), end='\n')
    
    # run the network on testing set
    a = forward_prop(network, te_set[0])
    acc = accuracy(np.argmax(a[-1], axis=1), np.argmax(te_set[1], axis=1))
    show_loginfo(log_type.info, "accuracy on TESTING set: {:.2f} %".format(100*acc))
    
    # run the network on validation set
    a = forward_prop(network, va_set[0])
    acc = accuracy(np.argmax(a[-1], axis=1), np.argmax(va_set[1], axis=1))
    show_loginfo(log_type.info, "accuracy on VALIDATION set: {:.2f} %".format(100*acc))
    
    # show the elapsed time
    show_loginfo(log_type.info, "time elapsed: {:.4f} sec".format(time.time()-start))
    return network


def init_network(x, y, n):
    """
    Initialize the network by taking the number of nodes in hidden layer.

    Arugments:
    ------
        x: feature matrix, each data is stored in row vetor, shape [N, 4]
        y: label matrix, each label is in row vector, shape [N, 3]
        n: list of number of nodes in hidden layers 
    
    Returns:
    ------
        network: list of weight matrix
    """
    show_loginfo(log_type.system, "Initilaizing network ...")
    show_loginfo(log_type.info, "Hidden layers: \n\t\t{}".format(n))

    w = [np.random.random([x.shape[1], n[0]])]
    for i in range(len(n)-1):
        w.append(np.random.random([n[i], n[i+1]]))
    w.append(np.random.random([n[-1], y.shape[1]]))
    return w

def back_prop_learning(x, y, alpha, network):
    """
    back propagation algorithm.

    Arugments:
    ------
        x: feature matrix, each data is stored in row vetor, shape [N, 4]
        y: label matrix, each label is in row vector, shape [N, 3]
        alpha : momentum
        network: list of weight matrix 
    
    Returns:
    ------
        network: list of weight matrix after update
        out: output of the network
    """
    a = forward_prop(network, x)

    # get delta by using properties of the sigmoid function
    delta = [a[-1] * (1-a[-1]) * (y - a[-1])]
    for i in range(len(network)-1, 0, -1):
        delta = [a[i] * (1-a[i]) * (delta[0] @ network[i].T)] + delta
    
    # update weight matrices by delta
    for i in range(len(network)):
        network[i] += alpha*(a[i].T @ delta[i])
    
    return network, a[-1]

def forward_prop(network, x):
    """
    forward propagation of the network. 

    Arguments
    ------
        network: list of weight matrix
        x: feature matrix
    Returns
    ------
        output of each layers in the network, list of numpy array
    """
    a = [x]
    for w in network:
        a.append(sigmoid(a[-1] @ w))
    return a

def accuracy(out, y):
    """
    calculate the accuracy of output of a network according to the truth. Onehot labels have shape (N, 3) while the arguments `out` and `y` should in the form of:
            np.argmax(onehot labels, axis=1) with shape (N, 1)

    Arguments
    ------
        out: array of output of a network
        y: array of true labels
    Returns
    ------
        accuracy in [0.0, 1.0]
    """
    diff = y - out
    p = diff[diff == 0].shape[0]/y.shape[0]
    return p

def get_output(a, labels):
    """
    decode the onehot labels into strings

    Arguments
    ------  
        a: output of the network in onehot form
        labels: all the labels possible in string
    Returns:
    ------
        label in string form
    """
    return labels[np.argmax(a)]

def sigmoid(x):
    return 1.0/(1.0+np.exp(-x))
