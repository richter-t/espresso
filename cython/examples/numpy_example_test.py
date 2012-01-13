import numpy as np
import os
import random
import numpy_example

x=np.zeros(10, dtype=int)
for i in range(10):
    x[i]=random.randint(0,20)
    
print x
print numpy_example.mysum(x)

test_array=np.zeros(10, dtype=int)
for i in range(10):
    test_array[i]=random.randint(0,20)

numpy_example.pointer_test(test_array) 
#numpy_example.pointer_test() 
