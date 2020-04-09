#Homework 3 Phys 3330

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import PIL

def matrixMult(A, B):
    rows = len(A)
    result = np.zeros((rows, rows))
    for i in range(rows):
        for j in range(rows):
            cellVal = 0
            for k in range(rows):
                cellVal = cellVal + A[i][k] * B[k][j]
            result[i][j] = cellVal
        
    
    print('Result =', result)

A = np.random.randint(low = 9, size = (3, 3))
B = np.linalg.inv(A)
print('A= ', A)
print('B= ', B)
matrixMult(A, B)

def sortArray(Arr):
    for i in range(len(Arr)):
        toSort = Arr[i]
        j = i-1
        while j >= 0 and toSort < Arr[j]:
            Arr[j+1] = Arr[j]
            j -= 1
        Arr[j + 1] = toSort
    print('\nSorted array: ', Arr)
            
randArray = np.random.randint(9, size=10)
print('Array to be sorted: ', randArray)
sortArray(randArray)

pic = mpimg.imread('iron-man.jpg')

bw_pic=np.zeros([np.size(pic,0),np.size(pic,1)])
for i in range(np.size(pic,0)):
    for j in range(np.size(pic,1)):
        bw_pic[i,j] = np.mean(pic[i,j])/255

x = np.sqrt(bw_pic)

plt.figure(1)
plt.title("Original")
imgplot = plt.imshow(pic)
plt.figure(2)
plt.title("Black and White")
imgplot1 = plt.imshow(bw_pic,cmap="gray")
plt.figure(3)
plt.title("Contrast Stretching")
imgplot2 = plt.imshow(x,cmap = "gray")
plt.figure(4)
plt.title("Histogram Original")
plt.hist(np.ravel(pic[:,:,0]),bins = 100,alpha = .33, color="r")
plt.hist(np.ravel(pic[:,:,1]),bins = 100,alpha = .33, color="g")
plt.hist(np.ravel(pic[:,:,2]),bins = 100,alpha = .33, color="b")
plt.figure(5)
plt.title("Grayscale Histogram")
plt.hist(np.ravel(bw_pic),bins=100)
plt.figure(6)
plt.title("Contrast Stretch Histogram")
plt.hist(np.ravel(x),bins = 100)
plt.show()
                

