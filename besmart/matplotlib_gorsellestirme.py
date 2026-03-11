import cv2 as cv
from matplotlib import pyplot as plt
path = r"C:\Users\beyza\Desktop\goruntu_isleme_dersi\image\opencv.png"
img = cv.imread(path)
gray=cv.imread(path, cv.IMREAD_GRAYSCALE)
rgb= cv.cvtColor(img, cv.COLOR_BGR2RGB)

# Çoklu görüntü gösterimi
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(rgb)
axes[0].set_title('Renkli (RGB)')
axes[0].axis('off')

axes[1].imshow(gray, cmap='gray')
axes[1].set_title('Gri Tonlama')
axes[1].axis('off')

axes[2].hist(gray.ravel(), 256, [0, 256])
axes[2].set_title('Histogram')

plt.tight_layout()
plt.show()