import numpy as np
import imageio.v3 as img
import matplotlib.pyplot as plt

# Membaca gambar
path = 'D:\\Perkuliahan\\S5\\Pengolahan Citra Digital\\s6\\tiger.jpg'
image = img.imread(path)

# Mendapatkan tinggi dan lebar gambar
height, width = image.shape[:2]

# Membuat gambar horizontal dan vertical kosong dengan ukuran yang sama seperti gambar asli
horizontal = np.zeros_like(image)
vertical = np.zeros_like(image)

# Proses membalikkan gambar secara horizontal
for y in range(height):
    for x in range(width):
        horizontal[y, x] = image[y, width - 1 - x]

# Proses membalikkan gambar secara vertikal
for y in range(height):
    for x in range(width):
        vertical[y, x] = image[height - 1 - y, x]

# Menampilkan gambar asli, gambar yang dibalik horizontal, dan yang dibalik vertikal
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(image)
plt.axis('off')  # Menghilangkan sumbu

plt.subplot(1, 3, 2)
plt.imshow(horizontal)
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(vertical)
plt.axis('off')

plt.show()
