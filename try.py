from PIL import Image
import numpy as np
from error_diffusion import ErrorDiffusion

image = Image.open("./assets/chrome_image.jpeg")


arr = np.array(image)

def diffusor(arr, f):
    for i in range(len(arr)): 
        for j in range(len(arr[i])): 
            current = arr[i][j]
            error = 0

            if current < f: 
                arr[i][j] = 0
            elif current > f: 
                arr[i][j] = 255
            
            error = current - arr[i][j]

            if j < len(arr[i]) - 1:
                arr[i][j+1] += error
    return arr

# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
i = 0
for idx, x in np.ndenumerate(arr): 
    print(idx, type(idx))
    i += 1
    print(x)
    # print(f{})
    print("--------")


# A = deffuser.one_way()

# arrA = np.array(A)

# print(arrA)

