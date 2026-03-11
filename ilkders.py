import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#1. görüntü okuma
# Örnek (Kendi dosya yoluna göre düzenle):
img = cv.imread(r"C:\Users\beyza\Desktop\goruntu_isleme_dersi\image\ornek1.jpg")

#2. görüntü griye dönüştü
gray= cv.imread("ornek1.jpg", cv.IMREAD_GRAYSCALE)
#3. görüntü bilgileri
print(f"boyutu: {img.shape}")
print(f"veri tipi: {img.dtype}")
print(f"toplam piksel: {img.size}")

#4. BGR -> RGB dönüşümü (matplotlib içindir)
img_rgb= cv.cvtColor(img, cv.COLOR_BGR2RGB)
#5. görüntüleme
plt.imshow(img_rgb)
plt.title("ilk görüntü")
plt. axis("off")
plt.show()
