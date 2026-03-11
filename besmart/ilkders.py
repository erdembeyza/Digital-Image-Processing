import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#1. görüntü okuma
# bilgisayardaki görselin yolunu py ortamına aktarır.
img = cv.imread(r"/image/ornek1.jpg")

#2. görüntü griye dönüştü

gray= cv.imread("ornek1.jpg", cv.IMREAD_GRAYSCALE)
#3. görüntü bilgileri
print(f"boyutu: {img.shape}") #(1080,1920,3) -> yükseklik, genişlik, kanal anlamına gelir
print(f"veri tipi: {img.dtype}") #piksel değerinin veri tipidir. uint8 olur genelde- 0-255
print(f"toplam piksel: {img.size}") #toplam piksel sayısıdır.

#4. BGR -> RGB dönüşümü (matplotlibe dönüşüm içindir)
#bu olmazsa eğer gökyüzü turuncu gibi renkler tersine döner
img_rgb= cv.cvtColor(img, cv.COLOR_BGR2RGB)

#5. görüntüleme
plt.imshow(img_rgb) #görüntüyü çizim alanına yerleştirir
plt.title("ilk görüntü")
plt. axis("off") #kenarlardaki x y koordinat çizgilerini gizler
plt.show() #hazırlanan pencereyi ekrana getirir

#gri tonlarında bir görsele ulaşmak istersem eğer kayıt edip yazdırmam gerekir