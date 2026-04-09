import cv2
import numpy as np
path= r"C:\Users\beyza\Desktop\goruntu_isleme_dersi\image\tuzbiber.png"
img= cv2.imread(path, 0)

# 1. Laplacian Kenar Algılama
laplacian = cv2.Laplacian(img, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))

# 2. Sobel X ve Y Gradyanları
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(sobelx, cv2.CV_64F, 0, 1, ksize=3)


# 3. Unsharp Masking
bulanik = cv2.GaussianBlur(img, (9, 9), 10.0)
keskin = cv2.addWeighted(img, 1.5, bulanik, -0.5, 0)

kernel_sharp = np.array([[ 0, -1,  0],
                          [-1,  5, -1],
                          [ 0, -1,  0]])
keskin2 = cv2.filter2D(img, -1, kernel_sharp)

cv2.imshow('orginal', img)
cv2.imshow('laplacian', laplacian)
cv2.imshow('sobelx', sobelx)
cv2.imshow('sobely', sobely)
cv2.imshow('keskin2', keskin2)
cv2.imshow('keskin', keskin)
cv2.waitKey(500)
cv2.destroyAllWindows()