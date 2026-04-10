import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
path = r"C:\Users\beyza\Desktop\goruntu_isleme_dersi\image\opencv.png"

img = cv.imread(path)
img_color=cv.imread(path, cv.IMREAD_COLOR)
img_gray= cv.imread(path, cv.IMREAD_GRAYSCALE )

# Define roi as an empty numpy array
roi = np.zeros((150, 200, 3), dtype=np.uint8)

# Resize roi to the desired dimensions
roi = cv.resize(roi, (200, 150))

# Assign roi to the specific region of img
img[0:150, 0:200] = roi

cv.imshow("Yapistirilmis", img)
dosya_adi = f"roi_cikarma.png"
cv.imwrite(dosya_adi, img)
cv.waitKey()
cv.destroyAllWindows()