import cv2
import numpy as np
path= r"C:\Users\beyza\Desktop\goruntu_isleme_dersi\ikinisan\belge.jpg"
img= cv2.imread(path)

binary = cv2.threshold(
    img, 127, 255, 
    cv2.THRESH_BINARY
)

# Otomatik Akıllı Eşik (Otsu)
otsu = cv2.threshold(
    img, 0, 255, 
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

cv2.imshow("orginal", img)
cv2.imshow("binary", binary[1])
cv2.imshow("otsu", otsu[1])
cv2.waitKey(0)
cv2.destroyAllWindows()