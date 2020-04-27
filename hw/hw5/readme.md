AI HW5 README
------------
Shang Wang

### Dependencies

OS: Window 10

python version 3.6.9

required package: `time`, `numpy`, `sys`, `os`

### How to Run

```
$ python3 main.py
```

### Expected Outputs

Training section:

```
[SYSTEM] Loading data set file
[SYSTEM] dataset file: 'ANN - Iris data.txt'
[INFO] Labels:
                ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
[INFO] Number of INPUT node: 
                4
[INFO] Number of OUTPUT node:
                3
[INFO] Train : Test : Validation
                60.00%, 20.00%, 20.00%
[SYSTEM] Initilaizing network ...
[INFO] Hidden layers:
                [5]
[INFO] Maximum iterations:
                10000
[SYSTEM] Training ... 
[INFO] accuracy on TRAINING set: 100.00 %
[INFO] accuracy on TESTING set: 96.67 %
[INFO] accuracy on VALIDATION set: 100.00 %
[INFO] time elapsed: 0.4718 sec
```
Mannually testing section:
```
[SYSTEM] Mannually input test data? [y or N]
 >>> y
[SYSTEM] Sepal length in cm:
 >>> 5.1
[SYSTEM] Sepal width in cm:
 >>> 3.5
[SYSTEM] Petal length in cm:
 >>> 1.4
[SYSTEM] Petal width in cm:
 >>> 0.2
[INFO] features input: 
                5.10, 3.50, 1.40, 0.20
[INFO] result:
                Iris-setosa

```

### File list

Folder:
* `dataset`: contains only the dataset file `ANN - Iris data.txt`
* `desctiption`: description of the problem
* `src`: source code of the ANN implementation 

Files:
* `src`:
  * `loginfo.py`: for colorful ternimal log message outputs.
  * `pre_process.py`: defined the function to read data from file in `dataset` folder, transfer the label column into onhot format, split the dataset into training set, testing set and validation set.
  * `ANN.py`: major implemenation of the back propagation learning algorithm for classification  

### Key components in ANN

#### Activation function

Sigmoid has the property that:
$$
g(x) = \frac{1}{1+e^{-x}}
$$
and its derivative: 
$$
g^\prime(x) = \frac{e^{-x}}{(1+e^{-x})^2} = g(x)[1-g(x)]
$$

#### Normalize the feature vector before training

As long as the physical meaning of the features requires a positive value, the noremalization of feature vector could be done by dividing the maximum of the each feature in the dataset. The normalization is implemented in the pre-process function. 

Therefore, in order to get the right class out of the network, the full procedure would be:

* normalize the individual test by the maximum vector in the dataset.
* forward propagating to get the outputs from the network.
* decode the outputs to get the label in string form.


#### Label and output formulation

The label set here is:
```
['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
```
By using onehot format: 
```
 'Iris-setosa'     -> [ 1, 0, 0 ] 
 'Iris-versicolor' -> [ 0, 1, 0 ] 
 'Iris-virginica'  -> [ 0, 0, 1 ] 
```

The labels are mapped from a string to a 3-vector of binary number. That is in the same scope of the output value of the sigmoid, thus, the feedback procedure could be implemented. 

Also, the output of the network need to be decoded from the onehot format to string. The value of the output vector of the network for an individual data is not necassarily a binary 3-vector. So, the index of the maximum value in the output will be used to find the coresponding string label in the labels above.

eg:
```
[0.11111, 0.22222, 0.5544543] -> [ 0, 0, 1 ]  -> 2 -> 'Iris-virginica'   
```


