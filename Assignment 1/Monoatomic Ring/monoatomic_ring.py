import os
import numpy as np
import matplotlib.pyplot as plt


def matrix(x,y,n):
    Y = []
    i = 0
    while i < n:
        X = []
        j = 0
        while j<n:
            X.append(0)
            j = j + 1
        Y.append(X)
        i = i + 1
    for i in range(n):
        for j in range(n):
            if (i == j):
                Y[i][j] = x
                if i == n-1:
                    break

                else:
                    Y[i+1][j] = y
                if j == n-1:
                    break
                else:
                    Y[i][j+1] = y
    Y[0][n-1] = y
    Y[n-1][0] = y
    return Y

def plot(x,y,n):
    Y = matrix(x,y,n)
    w,v = np.linalg.eig(Y)
    print("For x= {}, y= {}, n= {}, max eigenvalue= {} and min eigenvalue= {}".format(x,y,n,max(w),min(w)))
    wid = int(n)

    plt.hist(w, bins= wid)

    plt.xlabel('Eigenvalue')
    plt.ylabel('Density')
    plt.title('Monoatomic Ring N= {}, Beta= {}'.format(n,y))
    plt.savefig('MonoatomicRing N= {}, Beta= {}.pdf'.format(n,y))

plot(10, 0.1, 1000)
plot(10, 0.1, 500)
plot(10, 0.1, 250)
plot(10, 0.2, 1000)
plot(10, 0.3, 1000)


def density(x,y,n1,n2):
    X = []
    Y = []
    i = n1
    while i<n2:
        M = matrix(x,y,i)
        w,v = np.linalg.eig(M)
        band = max(w) - min(w)
        X.append(i)
        Y.append(band)
        i = i+1
    plt.plot(X,Y)
    plt.xlabel('N')
    plt.ylabel('Bandwidth')
    plt.title('N vs Bandwidth, Monoatomic Ring')
    plt.savefig('MonoatomicRing_bandwidth_N.pdf')

density(10, 0.1, 10, 100)


'''
Output:-

For x= 10, y= 0.1, n= 1000, max eigenvalue= 10.199999999999994 and min eigenvalue= 9.800000000000065
For x= 10, y= 0.1, n= 500, max eigenvalue= 10.199999999999969 and min eigenvalue= 9.800000000000093
For x= 10, y= 0.1, n= 250, max eigenvalue= 10.199999999999966 and min eigenvalue= 9.800000000000006
For x= 10, y= 0.2, n= 1000, max eigenvalue= 10.400000000000006 and min eigenvalue= 9.599999999999994
For x= 10, y= 0.3, n= 1000, max eigenvalue= 10.599999999999998 and min eigenvalue= 9.399999999999885
'''