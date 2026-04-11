"""fotoğrafı basitleştirerek "önemli olanı" (nesneyi) "önemsiz olandan" (arka plandan) ayırmaya yarayan 
en temel bölütleme (segmentasyon) tekniğidir.
Temel amacı karmaşık, çok renkli veya gri tonlamalı bir görüntüyü sadece siyah (0) ve beyaz (255) 
olmak üzere iki renge (ikili/binary formata) indirgemektir."""
import os
import cv2
import numpy as np
path= r"C:\Users\beyza\Desktop\goruntu_isleme_dersi\ikinisan\belge.jpg"
img= cv2.imread(path, 0)
binary = cv2.threshold(
    img, 127, 255, 
    cv2.THRESH_BINARY
)
# Otomatik Akıllı Eşik (Otsu)
otsu = cv2.threshold(
    img, 0, 255, 
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

cv2.imwrite(os.path.join(os.path.dirname(path), "binary.jpg"), binary[1])
cv2.imwrite(os.path.join(os.path.dirname(path), "otsu.jpg"), otsu[1])

cv2.imshow("orginal", img)
cv2.imshow("binary", binary[1])
cv2.imshow("otsu", otsu[1])
cv2.waitKey(0)
cv2.destroyAllWindows()