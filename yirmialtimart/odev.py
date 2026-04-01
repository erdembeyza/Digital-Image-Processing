import cv2
import numpy as np
path = r"C:\Users\beyza\Desktop\goruntu_isleme_dersi\yirmialtimart\manzara.jpg"
img= cv2.imread(path)

y,x =img.shape[:2]
maske=np.zeros((y,x), dtype=np.uint8)
merkez_x=x//2
merkez_y=y//2

yaricap=int (min(x,y)* 0.4)
cv2.circle(maske,(merkez_x,merkez_y),yaricap,255,-1)

vignette=cv2.bitwise_and(img, img, maske=maske)
M_dondurma=cv2.getRotationMatrix2D((merkez_x,merkez_y),-15,1.0)
sonuc= cv2.warpAffine(vignette,M_dondurma,(x,y), flags=cv2.INTER_LINEAR)
cv2.imshow('orijinal', img)
cv2.imshow('maskeleme', maske)
cv2.imshow('vignette/maske', vignette)
cv2.imshow("dondurulmus_sonuc", sonuc)

cv2.waitKey(0)
cv2.destroyAllWindows()