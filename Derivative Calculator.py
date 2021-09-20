import math

x0 = float(input())

for i in range(-20, 0):
    h = 10**i
    y = 2 * math.cos(x0 + h/2) * math.sin(h/2) / h
    value = round(y, 7)
    print("When h = 1e" + str(i) + ", value:", value)

