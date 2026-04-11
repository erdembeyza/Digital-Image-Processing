import os

import cv2
import numpy as np
import matplotlib.pyplot as plt

#1)Görüntü matris boyutunu Numpy ile printleyin.
path = r"C:\Users\beyza\Desktop\goruntu_isleme_dersi\ikinisan\xray.jpg"
img = cv2.imread(path, 0) 
print(img.shape)
#sonuc: 415, 720

#2) Görüntüye hem standart global `cv2.equalizeHist()` uygulayın, hem de el ile matematiksel Logaritmik Dönüşüm Numpy Matris Operasyonu
global_eq = cv2.equalizeHist(img)

# Slayttan-> Logarithmic Transform (Normalizasyon Taktikli)
c = 255 / np.log(1 + np.max(img))
log_img = c * (np.log(img.astype(np.float64) + 1))
log_img = np.array(log_img, dtype=np.uint8)

#3) Matplotlib kütüphanesinin `subplots` alanını kullanarak 1 Satır, 3 Sütunlu bir çıktı (Orijinal, Log, GlobalEQ) elde ediniz.
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(img, cmap='gray')
axes[0].set_title('Orijinal')
axes[1].imshow(log_img, cmap='gray')
axes[1].set_title('Logaritmik')
axes[2].imshow(global_eq, cmap='gray')
axes[2].set_title('GlobalEQ')
plt.show()

# Görüntüleri kaydet

cv2.imwrite(os.path.join(os.path.dirname(path), "global_eq.jpg"), global_eq)
cv2.imwrite(os.path.join(os.path.dirname(path), "logaritmik.jpg"), log_img)
cv2.imwrite(os.path.join(os.path.dirname(path), "orijinal.jpg"), img)

#4) Notebook Raporunuza Ekleyiniz: Çıktıdaki siyah arka plana ne oldu? Hangi yöntem daha fazla gürültü üretti, bunun teorik altyapısı nedir?
"""Arka plandaki karanlık kısımlar yumuşak şekilde aydınlandı. Tam siyahlar yine tam siyah (0) olarak
kalmaya devam etti. Böylelikle kemik ve doku detayları görünür  haldeyken arka plan bütünlüğü bozulmamış oldu.
Daha fazla gürültü üreten kısım global histogram eşitlemedir. Xray gibi tıbbi görüntülerde arka plan 
devasa bir homojen bölge oluşturur. Bu yüzden görüntüdünün histogram grafiğğinde siyah tonuna yakın yüksek sütun 
yığılması gözlemlenmektedir.
"""