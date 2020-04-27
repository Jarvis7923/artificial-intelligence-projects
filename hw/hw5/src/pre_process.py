"""
This script is for reading the data from file in folder `/dataset', and normalize the feature data as well as transfering string label to onehot data format. Also split the dataset into training, testing and validation sets. 

author: shang wang
id: 1277417
email: swang27@tufts.edu

"""

import os
import numpy as np

from src.loginfo import show_loginfo, log_type

def get_data():
    """
    Read the dataset file located at `/dataset'. Empty and multiple files could not be recogonized. Returns to a numpy array contains all the elements in row vectors. Each elemens are stacking features and onehot labels in [ features | labels ].  

    Returns
    -------
        np.array(dtype=np.float): the data set after transfering to onehot data format
   
    """

    show_loginfo(log_type.system, "Loading data set file")
    path = r'dataset/'
    files = os.listdir(path)
    if len(files) == 0:
        show_loginfo(log_type.error, "No data set files found!")
        return False
    
    if len(files) > 1:
        show_loginfo(log_type.error, "To much data set file!")
        return False
   
    ds = files[0] 
    show_loginfo(log_type.system, "dataset file: \'{}\'".format(ds))

    with open(path + ds) as f:
        data = f.read().splitlines()
    try:
        data.remove('')
    except Exception:
        pass

    x, y = [], []
    for i in range(len(data)):
        ele = data[i].split(',')
        x.append(ele[:-1])
        y.append(ele[-1])

    labels = list(set(y))
    show_loginfo(log_type.info, "Labels: \n\t\t{}".format(labels))
    for j in range(len(y)):
        y[j] = onehot(y[j], labels)
    
    x, y = np.asfarray(x), np.asfarray(y)
    show_loginfo(log_type.info, "Number of INPUT node: \n\t\t{}".format(x.shape[1]))
    show_loginfo(log_type.info, "Number of OUTPUT node: \n\t\t{}".format(y.shape[1]))
    return np.c_[x, y], labels

def get_datasets(ratio):
    """
    Normalize the features, and split and shuffle the raw dataset according to ratio.

    Returns
    -------
        (tr_set, te_set, va_set, labels, x_max)
        
        tr_set: training set, a tuple (features, lables), 
        te_set, tr_set: for testing set and validation set in the same format
        labels: the set of labels in string
        x_max: a array of max value in each feature, useful for normalization

    """
    res = get_data()
    if res is not False:
        data, labels = get_data()
    else:
        return False

    r_tr, r_te, r_va = ratio
    n = r_tr+r_te+r_va
    show_loginfo(log_type.info, "Train : Test : Validation\n\t\t{0[0]:.2f}%, {0[1]:.2f}%, {0[2]:.2f}%".format(np.asanyarray(ratio)/n*100))

    n_labels = len(labels)
    
    x_max = np.max(data[:, :-n_labels], axis=0)
    data[:, :-n_labels] = data[:, :-n_labels]/x_max

    s = []
    for i in range(1, n_labels+1):
        s.append( data[ data[:,-i] == 1, :] )
    
    tr, te, va = [], [], [] 
    
    for ele in s:
        N = len(ele)/(r_tr+r_te+r_va)
        n_tr, n_te, n_va = int(N*r_tr), int(N*r_te), int(N*r_va)
        tr.append(ele[:n_tr, :])
        te.append(ele[n_tr:n_tr+n_te, :])
        va.append(ele[n_tr+n_te:, :])

    dsets = [tr, te, va]
    for i in range(len(dsets)):
        d = np.vstack(dsets[i])
        np.random.shuffle(d)
        dsets[i] = (d[:,:-n_labels], d[:,-n_labels:] )
    return tuple(dsets + [labels] + [x_max])

def onehot(s, labels):
    """
    onehot formalization for all the labels. 
        eg. labels = ['Iris-versicolor', 'Iris-virginica', 'Iris-setosa']
            s = 'Iris-vesicolor' -> return [1, 0, 0]
            s = 'Iris-virginica' -> return [0, 1, 0]
            s = 'Iris-setosa'    -> return [0, 0, 1]
    
    Arguments
    -------
        s: current label in string
        labels: list of all possible labels in string
    Returns
    -------
        onehot format of s in terms of labels
    """
    f = [0]*len(labels)
    f[labels.index(s)] = 1
    return f

