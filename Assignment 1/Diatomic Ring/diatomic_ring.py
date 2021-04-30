import os
import numpy as np
import matplotlib.pyplot as plt


def matrix(x,y,z,n):
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
                if i >= n-1:
                    break
                else:
                    Y[i+1][j] = y
                if j >= n-1:
                    break
                else:
                    Y[i][j+1] = y

    i = 0
    while i<n:
        Y[i][i] = z
        i = i + 2
       
    Y[0][n-1] = y
    Y[n-1][0] = y
    i = 0
    j = 0  

    return Y

def plot(x,y,z,n):
    Y = matrix(x,y,z,n)
    w,v = np.linalg.eig(Y)
    print("For x= {}, y= {}, z= {}, n= {}, max eigenvalue= {} and min eigenvalue= {}".format(x,y,z,n,max(w),min(w)))
    wid = int(n)

    plt.hist(w, bins= wid)
    plt.xlabel('Eigenvalue')
    plt.ylabel('Density')
    plt.title('Diatomic Ring N = {}, Beta = {}'.format(n,y))
    plt.savefig('DiatomicRing N = {}, Beta = {}.pdf'.format(n,y))


plot(10, -2, 5, 1000)
plot(10, -2, 5, 500)
plot(10, -2, 5, 250)
plot(10, -1, 5, 1000)
plot(10, -0.5, 5, 1000)


'''
Output:

For x= 10, y= -2, z= 5, n= 1000, max eigenvalue= 12.216990566028313 and min eigenvalue= 2.7830094339716913
For x= 10, y= -2, z= 5, n= 500, max eigenvalue= 12.21699056602832 and min eigenvalue= 2.783009433971678
For x= 10, y= -2, z= 5, n= 250, max eigenvalue= 12.216990566028302 and min eigenvalue= 2.7830094339717157
For x= 10, y= -1, z= 5, n= 1000, max eigenvalue= 10.701562118716415 and min eigenvalue= 4.298437881283575
For x= 10, y= -0.5, z= 5, n= 1000, max eigenvalue= 10.192582403567263 and min eigenvalue= 4.80741759643275
'''