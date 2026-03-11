import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
"""--Cv Penceresi İle Gösterme--"""
path= r"C:\Users\beyza\Desktop\goruntu_isleme_dersi\image\ornek1.jpg"
src= cv.imread(path)
cv.imshow("pencere_adı", src)
cv.waitKey()


"""--Boyutlandırarak Gösterme--"""
#kullanıcı istediği gibi genişletip daraltabilir görseli
cv.namedWindow("resim1", cv.WINDOW_NORMAL)
cv.resizeWindow("resim1", 800,600)
cv.imshow("resim1", src)
cv.waitKey()
#pencere isimleri aynı olmalıdır.

"""--Görüntü Kaydetme--"""
#Farklı formatta kaydetme
cv.imwrite("besmart/resim.png", src) #ornek1.jpg dosyasını resim.png olarak kaydeder
#JPG kalite ayarı
cv.imwrite('besmart/kaliteli.jpg', src,
           [cv.IMWRITE_JPEG_QUALITY, 95])
#oluşan görsel çıktılarını image dosyasına kayıt olmasını istiyorsan
# 'image' klasörünün içine 'kaliteli.jpg' olarak kaydeder
#cv2.imwrite('image/kaliteli.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 95]) olarak değiştirmelisin

#PNG sıkıştırma seviyesi
cv.imwrite("besmart/sk.png", src, [cv.IMWRITE_PNG_COMPRESSION, 9])
cv.destroyAllWindows()