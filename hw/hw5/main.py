"""
Testing scripts with user interface to test individual data

author: shang wang
id: 1277417
email: swang27@tufts.edu

"""

import numpy as np
import sys

from src.pre_process import get_datasets
import src.ANN as ANN
from src.loginfo import show_loginfo, log_type

if __name__ == "__main__":
    res = get_datasets(ratio=[3, 1, 1])
    if res is not False:
        tr_set, te_set, va_set, labels, x_max = res
    else:
        show_loginfo(log_type.system, r"Ending ... ", end='\n')
        sys.exit()
        
    network = ANN.run(tr_set, te_set, va_set, 
                        layers=[5], alpha=0.6, iter=10000)

    features = [
        r'Sepal length in cm',
        r'Sepal width in cm',
        r'Petal length in cm',
        r'Petal width in cm'
    ]
    show_loginfo(log_type.system, r"Mannually input test data? [y or N]",'\n >>> ' )
    m = input('').strip().lower()
    while (m == 'y') or (m == 'yes'):
        x = np.zeros(len(features))
        for i in range(len(features)):
            show_loginfo(log_type.system, features[i] + ':', end='\n >>> ')
            x[i] = float(input(''))
        show_loginfo(log_type.info, 'features input: \n\t\t{0[0]:.2f}, {0[1]:.2f}, {0[2]:.2f}, {0[3]:.2f}'.format(x),end='\n')
        a = ANN.forward_prop(network, x/x_max)
        res = ANN.get_output(a[-1], labels)
        show_loginfo(log_type.info, 'result: \n\t\t{}'.format(res))
        
        show_loginfo(log_type.system, r"Mannually input test data? [y or N]", end='\n >>> ')
        m = input('').strip().lower()
    show_loginfo(log_type.system, r"Ending ... ", end='\n')

        

    
