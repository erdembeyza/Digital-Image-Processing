import cv2 as cv 
import numpy as np
path= r"C:\Users\beyza\Desktop\goruntu_isleme_dersi\ikinisan\sisli.jpg"
img= cv.imread(path)
# Min ve Max tonları bul ($r_{min}$, $r_{max}$)
min_val = np.min(img)
max_val = np.max(img)

# Formül: (r - min) / (max - min) * 255
katsayi = 255.0 / (max_val - min_val)
stretched = (img - min_val) * katsayi

# Sonucu tam sayı 8-bit renk formatına çevir
stretched = np.uint8(stretched)

cv.imshow("orginal", img)
cv.imshow("stretched", stretched)
cv.waitKey()