import cv2 as cv
from matplotlib import pyplot as plt
path = r"C:\Users\beyza\Desktop\goruntu_isleme_dersi\image\opencv.png"

img_color=cv.imread(path, cv.IMREAD_COLOR)
img_gray= cv.imread(path, cv.IMREAD_GRAYSCALE )

print(f"renkli boyut: {img_color.shape}")
print(f"gri boyut:{img_gray.shape}")

for bit in[8,4,2,1]:
    seviye=2**bit
    faktor=256//seviye
    nicemli=(img_gray//faktor)*faktor
   
    dosya_adi = f"{seviye} Seviye ({bit}-bit).png"
    cv.imwrite(dosya_adi, nicemli)

    cv.waitKey()
    cv.destroyAllWindows()