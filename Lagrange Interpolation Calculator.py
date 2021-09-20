import sys
import numpy as np
sys.stdin = open("lagrange-input.txt", "r")

n = int(input())
x = np.zeros((n))
y = np.zeros((n))

for i in range(n):
    x[i], y[i] = [float(i) for i in input().split()]

for i in range(n):
    yy = 0
    print("     ", end="")
    for j in range(n):
        if j != i:
            s = "(x - " + str(x[j]) + ") * "
            print(s, end="")
            yy += len(s)      
    print(y[i], "\n", i, " "*(5-len(str(i))), "-" * yy, "\n","     ", end="", sep="")
    for j in range(n):
        if j != i:
            print("(" + str(x[i]) + " - " + str(x[j]) + ") * ", end="")  
    print("\n\n")

xp = float(input())
yp = 0
for i in range(n):
    p = 1
    for j in range(n):
        if i != j:
            p *= (xp - x[j])/(x[i] - x[j])
    yp += p * y[i]    
print('lagrange value at %.3f is %.3f.\n\n' % (xp, yp))
