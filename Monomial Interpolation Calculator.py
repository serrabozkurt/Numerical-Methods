import sys
import numpy as np
sys.stdin = open("monomial-input.txt", "r")

n = int(input())
x = [0]*n
fx = [0]*n

for i in range(n):
    x[i], fx[i] = [int(i) for i in input().split()]

l = [[0 for i in range(n)] for i in range(n)]

for i in range(n):
    a = 1
    for j in range(n):
        l[i][j] = a
        a *= x[i]

a = np.array(fx)
b = np.array(l)
x = np.linalg.solve(b, a)
print("VANDERMONDE: \n" ,b, "\n\nfx: ", a,"\n\nsolution: ", x, sep="")

a = x[0]
xpf = float(input())
xp = xpf

for i in range(n-1):
    a += (x[i+1]*xp)
    xp *= xpf
print('monomial value at %.3f is %.3f.\n\n' % (xpf, a))

