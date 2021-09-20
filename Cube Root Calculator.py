def cube_root_finder(y):
    a, e = y, 0

    while a >= 1:
        a /= 2
        e += 1

    const1, const2, const3 = 2/3, 2**(1/3), a**(1/3)

    x = 2 ** (e//3) #apply integer division to e
    #and then check get the power of remaining modulus part
    x *= (2 ** ((e % 3)/3))

    return x * const3

print("Cube root =", cube_root_finder(float(input("Input a float: "))))