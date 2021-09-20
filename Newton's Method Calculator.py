import numpy as np
import sys
sys.stdin = open("newton-input.txt", "r")

n = int(input())
x = np.zeros((n))
f_x = np.zeros((n))

for i in range(n):
    x[i], f_x[i] = [float(i) for i in input().split()]


liste, newtonlist_tp = [], []
liste += [[1]*len(x)]

for i in range(len(x)-1):
    newliste = []
    for j in range(len(x)):
        newliste += [x[j] - x[i]]

    liste += [newliste]


for i in range(len(x)):
    sumliste = []
    for j in range(len(x)):
        sumliste += [liste[i][j]]
    

    if i != 0:
        for j in range(len(x)):
            sumliste[j] *= newtonlist_tp[-1][j]

    newtonlist_tp += [sumliste]


newtonlist = np.transpose(newtonlist_tp)
f_x = np.array(f_x)
solution = np.linalg.solve(newtonlist, f_x)

print("fi tablosu:\n", newtonlist, "\n\nf_x tablosu: ", f_x, 
"\n\nsolution: ", solution ,"\n\n", sep="")

xp = float(input())
yp = solution[0]

for i in range(n-1):
    anyth = solution[i+1]
    for j in range(i+1):
        anyth *= (xp-x[j])
    yp += anyth
print('newton value at %.3f is %.3f.\n\n' % (xp, yp))




