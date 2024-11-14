import numpy as np
import imageio.v3 as img
import matplotlib.pyplot as plt

path = 'D:\\Perkuliahan\\S5\\Pengolahan Citra Digital\\s6\\tiger.jpg'
image = img.imread(path)

height, width = image.shape[:2]

# Buat array kosong untuk menyimpan gambar yang sudah dimirror
mirrored = np.zeros_like(image)

# Melakukan mirroring horizontal dan vertikal dalam satu loop
for y in range(height):
    for x in range(width):
        mirrored[y, x] = image[height - 1 - y, width - 1 - x]

plt.figure(figsize=(10, 5))

# Menampilkan gambar asli, gambar hasil mirroring horizontal, dan gambar hasil mirroring vertikal
plt.subplot(1, 3, 1)
plt.imshow(image)
plt.axis('off')

# Menampilkan gambar yang sudah dimirror
plt.subplot(1, 3, 2)
plt.imshow(mirrored)
plt.axis('off')

plt.show()
