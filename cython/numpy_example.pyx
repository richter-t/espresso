cimport numpy

def mysum(numpy.ndarray a):
    #cast to c style pointer
    cdef double *p = <double *>a.data
    cdef double s=0
    for i from 0<=i < len(a):
                s += p[i]
    p[0] = 13.
    return s

