import cv2
import numpy as np
path= r"C:\Users\beyza\Desktop\goruntu_isleme_dersi\image\tuzbiber.png"
img= cv2.imread(path, 0)
# 1. Kutu (Ortalama) Filtre
kutu = cv2.blur(img, (5, 5))

# 2. Gauss Filtre
gauss = cv2.GaussianBlur(img, (5, 5), 0)

# 3. Medyan Filtre
medyan = cv2.medianBlur(img, 5)  # ksize tek sayı!

# 4. Bilateral Filtre (Kenar koruyucu)
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

# 5. Özel kernel ile filtreleme
kernel = np.ones((7,7), np.float32) / 25
ozel = cv2.filter2D(img, -1, kernel)

cv2.imshow("orginal", img)
cv2.imshow("kutu", kutu)
cv2.imshow("gauss", gauss)
cv2.imshow("medyan", medyan)
cv2.imshow("bilateral", bilateral)
cv2.imshow("ozel", ozel)
cv2.waitKey(0)
cv2.destroyAllWindows()

#kendin de filtre kernel oluşturabilirsin