import numpy as np
import matplotlib.pyplot as plt
import os
from skimage.metrics import structural_similarity

def combine(U, S, V):
   return np.dot(np.dot(U, S), V)

def svd_compress(img, k): # compressing a given image
   
    U, singular_vals, V = np.linalg.svd(img)

    # for this question's case, no rank will be overflowed, but anyway, just to check:
    if k > len(singular_vals):
        print("Given compression rank is larger than rank of the original image!! No compression possible!!\n")
        return img

    U = U[:,:k] # take columns less than k from U
    V = V[:k,:] # take rows less than k from V
    S = np.diag(singular_vals)
    S = S[:k,:k]

    print("When compressed image's rank =", k)
    print("SHAPES: U: {0}, S: {1}, V: {2}".format(U.shape, S.shape, V.shape))

    compressed = combine(U, S, V)

    # to see the structural similarities between the real image and compressed one
    ss = structural_similarity(img, compressed, data_range=img.shape[1]) 
    print ("Strucural similarity =", ss)
    
    return compressed


img = plt.imread("clown.bmp")
print("Original image dimensions", img.shape)
print("\nIn this code we will view strucural similarities between original image and compressed images as an indicator for performance of the truncated SVD)")

r, i = 2, 1
fig = plt.figure()

while r < 128:

    compressed = svd_compress(img, r)
    fig.add_subplot(3, 2, i)

    plt.imshow(compressed, cmap = "gray")

    plt.imsave("clown_with_rank_" + str(r) + ".png", compressed, cmap = "gray")
    print("Size of the compressed image:", os.path.getsize("clown_with_rank_" + str(r) + ".png")/1024,'\n')
    r *= 2
    i += 1

plt.show()
fig.savefig("all_clowns.png")
plt.close()

print("As you can see from the shapes of U, S and V, the sizes of each U is m*r and sizes of each S is r*1 and sizes of each V is r*n \nStorage used for each image as a function of r: f(r) = r * (m + n + 1)")
print("As you can see from the sizes of each compressed image, it gets increased when the rank increases")

