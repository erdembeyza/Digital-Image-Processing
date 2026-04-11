import os

import cv2
import numpy as np
path= r"C:\Users\beyza\Desktop\goruntu_isleme_dersi\yirmialtimart\karanlik.jpg"
img= cv2.imread(path, 0)

negatif = 255 - img

# 2. Logarithmic Transform (Normalizasyon Taktikli)
c = 255 / np.log(1 + np.max(img))
log_img = c * (np.log(img.astype(np.float64) + 1))
log_img = np.array(log_img, dtype=np.uint8)

# 3. Gamma Transform: Lookup Table (LUT) Hızlandırıcısı PÜF NOKTASI!
gamma = 0.4 # Pikseller açılır/aydınlanır
# Her bir milyon piksel için kuvvet işlemi yapmak GPU/CPU düşmanıdır!
# LUT: Her seferinde hesaplamak yerine önce bir tablo yaratıp sonra saniyede eşleştirir:
lookUpTable = np.array([((i / 255.0) ** gamma) * 255
                        for i in np.arange(0, 256)]).astype("uint8")
gamma_img = cv2.LUT(img, lookUpTable)


#sonuçları kaydet
output_folder = os.path.dirname(path)
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

cv2.imwrite(os.path.join(output_folder, "negatif.jpg"), negatif)
cv2.imwrite(os.path.join(output_folder, "log.jpg"), log_img)
cv2.imwrite(os.path.join(output_folder, "gamma.jpg"), gamma_img)

#sonuçları göster
cv2.imshow("negatif", negatif)
cv2.imshow("log", log_img)
cv2.imshow("gamma", gamma_img)
cv2.waitKey()
cv2.destroyAllWindows()
