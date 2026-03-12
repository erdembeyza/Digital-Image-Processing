import cv2 as cv
from matplotlib import pyplot as plt
path = r"C:\Users\beyza\Desktop\goruntu_isleme_dersi\image\opencv.png"

img_color=cv.imread(path, cv.IMREAD_COLOR)
img_gray= cv.imread(path, cv.IMREAD_GRAYSCALE )

print(f"renkli boyut: {img_color.shape}")
print(f"gri boyut:{img_gray.shape}")

for olcek in [1,0.5,0.25,0.125]:
    kucuk=cv.resize(img_gray,  None, fx=olcek, fy=olcek, interpolation=cv.INTER_NEAREST)
    buyuk=cv.resize(kucuk, img_gray.shape[::1], interpolation=cv.INTER_NEAREST)
    cv.imshow(f"olcek: {olcek}", buyuk)
    cv.waitKey()
