import cv2 as cv
from matplotlib import pyplot as plt
path = r"C:\Users\beyza\Desktop\goruntu_isleme_dersi\image\opencv.png"
img = cv.imread(path)
img_color=cv.imread(path, cv.IMREAD_COLOR)
img_gray= cv.imread(path, cv.IMREAD_GRAYSCALE )

roi = img[50:200, 100:300]
cv.imshow("ilgi alanı çıkarma", roi)
img[0:150,0:200]=roi
cv.waitKey()