import cv2 as cv
import numpy as np

img=np.zeros((512,512,3), dtype="uint8")
img=cv.resize(img, (300,300))
cv.imshow("siyah kare", img)


cv.rectangle(img, (384, 0), (100,100), (0, 255, 0), 3)
cv.waitKey()