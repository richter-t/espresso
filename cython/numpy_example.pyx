cimport numpy as np
import numpy as np
import random

def mysum(np.ndarray a):
    #cast to c style pointer
    cdef int*p = <int *>a.data
    cdef int s=0
    for i from 0<=i < len(a):
                s += p[i]
    return s

def pointer_test(np.ndarray python_a):
    cdef long *p
    p2c=0
    c2p=0

    print "python array: "
    print python_a
    print
    #actual conversion from ndarray to c style pointer
    #only works when the array is defined as argument to 
    #the function! may not be portable<
    p=<long *> python_a.data
    print "data from pointer"
    for i from 0<=i<10:
        printf("%d ", p[i])

    for i from 0<=i<10:
        if p[i]!=python_a[i]:
            p2c=1

    print
    print "conversion pointer to python"
    print "pointer data"
    #backwards conversion pointer to ndarray
    for i from 0<=i<10:
        p[i]=random.randint(0, 20)
        printf("%d ", p[i])
        python_a[i]=p[i]

    for i from 0<=i <10:
        if p[i]!=python_a[i]:
            c2p=1

    #not possible
    #python_a.data=<np.ndarray > p

    print 
    print "python array"

    print python_a

    if p2c==1:
        print "python to c failed"
    else:
        print "python to c ok"

    if c2p==1:
        print "c to python failed"
    else:
        print "c to python ok"
