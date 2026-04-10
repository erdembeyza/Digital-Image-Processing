import cv2
import numpy as np
path = r"C:\Users\beyza\Desktop\goruntu_isleme_dersi\image\opencv.png"
img = cv2.imread(path)
# Tek piksel erişimi (satır, sütun)
piksel = img[100, 200]            # [B, G, R] değerleri
print(f"Piksel (100,200): {piksel}") # örn: [142, 180, 215]

# Tek kanal erişimi
mavi = img[100, 200, 0]   # B kanalı
yesil = img[100, 200, 1]  # G kanalı
kirmizi = img[100, 200, 2] # R kanalı

# Piksel değeri değiştirme
img[100, 200] = [255, 255, 255]  # Beyaz yap

# ROI (Region of Interest) – İlgi Bölgesi
roi = img[50:200, 100:300]      # Dikdörtgen bölge kesme

# 2. ROI'nin gerçek boyutlarını alıyoruz
yukseklik, genislik, kanal = roi.shape
# 3. Yapıştırırken bu boyutları kullanıyoruz
# Böylece hedef alan tam olarak ROI boyutunda olur
img[0:yukseklik, 0:genislik] = roi
cv2.imshow("Yapistirilmis", img)
cv2.waitKey(0)

# Kanal ayırma ve birleştirme
b, g, r = cv2.split(img)
birlesik = cv2.merge([b, g, r])