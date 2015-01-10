#!/usr/bin/python

from math import sqrt, floor

from project_euler import timeit


def test_eq(x,y,D):
    if (x**2) == 1+(D*(y**2)):
        return True
    return False


def pell(D):
    m = [0,]
    d = [1,]
    a = [floor(D**0.5),]
    A = [a[0],]
    B = [1,]

    for n in xrange(0,10000):
        if test_eq(A[n],B[n], D):
            return A[n],B[n],D

        m.append(int( (d[n]*a[n]) - m[n] ))
        d.append(int( (D - (m[n+1])**2)/d[n] ))
        a.append(int( floor((a[0]+m[n+1])/d[n+1]) ))

        if n == 0:
            A.append(int( a[0]*a[1] + 1 ))
            B.append( a[1] )
        else:
            A.append(int( a[n+1]*A[n] + 1*A[n-1] ))
            B.append(int( a[n+1]*B[n] + 1*B[n-1] ))

    return None


def convergents_of_e():
    answer = (0,0)
    for x in range(1,1001):
        if x**0.5 != int(x**0.5):
            res = pell(x)
            if res[0] > answer[0]:
                answer = res

    return answer[-1]


timeit(convergents_of_e)
