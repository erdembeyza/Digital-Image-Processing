import os
"""standart histogram: görüntünün tamamına (global) bakar ve karanlık fotoğrafları aydınlatmak veya 
soluk fotoğrafların kontrastını artırmak için pikselleri 0-255 arasına yayar.
clache: sh nin yapamadığı kısımları yapar: lokal kontrast artırma, gürültü koruma, aşırı aydınlatılmış 
bölgeleri tıraşlama gibi işlemleri yapar."""

import cv2
import numpy as np
path= r"C:\Users\beyza\Desktop\goruntu_isleme_dersi\ikinisan\sisligece.jpg"
img= cv2.imread(path, 0)
"""burdaki 0ı unutma!"""

hist_data = cv2.calcHist([img], [0], None, [256], [0, 256])
# Kolayı: plt.hist(img.ravel(), 256, [0, 256]) 

# 2. Global Histogram Eşitleme (Zararlı olabilir)
global_eq = cv2.equalizeHist(img)

# 3. CLAHE (Modern Sektör Standardı - Gürültü Koruyucu)
# clipLimit: Tıraşlanacak max frekans. tileGridSize: lokal fayans matris
clahe_obj = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_img = clahe_obj.apply(img)

cv2.imwrite(os.path.join(os.path.dirname(path), "global_eq.jpg"), global_eq)
cv2.imwrite(os.path.join(os.path.dirname(path), "clahe.jpg"), clahe_img)

cv2.imshow('orginal', img)
cv2.imshow('CLAHE (Mucize!)', clahe_img)
cv2.waitKey(0)
