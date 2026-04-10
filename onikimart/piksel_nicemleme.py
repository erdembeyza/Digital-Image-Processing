import cv2
import numpy as np
img = cv2.imread(r'c:\Users\beyza\Desktop\goruntu_isleme_dersi\onikimart\vesikalik.jpg', cv2.IMREAD_GRAYSCALE)

# 1. Görüntüyü gri tonlamalı (Grayscale) olarak yükle

# 2. ÖRNEKLEME: Görüntüyü küçülterek pikselleştir (Örn: 20x20 piksel)
h, w = img.shape[:2]
temp = cv2.resize(img, (20, 20), interpolation=cv2.INTER_LINEAR)

# 3. NİCEMLEME: Gri seviye sayısını 16'ya düşür (Quantization)
# Formül: floor(pixel / (256/L)) * (256/L)
levels = 16
quantized = (temp // (256 // levels)) * (256 // levels)

# 4. EN SAĞDAKİ MATRİS GÖRÜNÜMÜ: Sayısal değerleri ekrana bas
print("Piksel Matrisi (Sayısal Görünüm):")
print(quantized)

# 5. BLOKLU GÖRÜNÜM: Tekrar orijinal boyuta büyüt (INTER_NEAREST ile)
pixelated_view = cv2.resize(quantized, (w, h), interpolation=cv2.INTER_NEAREST)

cv2.imshow('Pixelated', pixelated_view)
cv2.waitKey(0)