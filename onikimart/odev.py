#vesikalık griye çevir
#görüntü matris boyutlarını analiz edip print ver
#sadece yüzü kapsayan bölgeyii roi slicing keserek ayır
#kesilen yüzü numpy matrisi ile 2bit(4renk) olacak şekilde yuvarlama faktörü ile nicemle
import cv2
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow

img_renkli= cv2.imread("vesikalik.jpg", cv2.IMREAD_COLOR)
img_gri= cv2.imread("vesikalik.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("renkli vesikalik", img_renkli)
cv2.imshow("gri vesikalik", img_gri)
cv2.waitKey()
"--------"
print(f"renkli{img_renkli.shape}")
print(f"gri{img_gri}")
"--------"
#ilk olarak koordinatları belirlemek gerekir
#matplot kütüphanesi yaptığımız içinde de görüntünün rengini ayarlamalıyız
img_rgb=cv2.cvtColor(img_renkli, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.show()
#400:800 x ekseninde, 270:790 y ekseninde
face=img_renkli[270:790, 400:800]
cv2.imshow("yuz", face)
cv2.waitKey()
"-------"
#nicemleme
bit=2
seviye=2**bit
faktor=256//seviye
yuz_bit=(face//faktor)*faktor
cv2.imshow(f'{seviye}Seviye ({bit}-bit)', yuz_bit)
cv2.waitKey()
cv2.destroyAllWindows()