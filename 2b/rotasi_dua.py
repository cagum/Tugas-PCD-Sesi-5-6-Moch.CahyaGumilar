import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

def rotateImage(image, degree):
    radian_deg = np.radians(degree)
    cos_deg, sin_deg = np.cos(radian_deg), np.sin(radian_deg)
    
    height, width = image.shape[:2]
    max_dim = int(np.sqrt(height**2 + width**2))  # Ukuran maksimal gambar setelah rotasi
    outputImage = np.zeros((max_dim, max_dim, 3), dtype=image.dtype)
    
    # Proses rotasi citra dengan pivot di titik (0,0)
    for y in range(height):
        for x in range(width):
            # Rotasi berdasarkan formula matriks rotasi 2D
            newX = int(cos_deg * x - sin_deg * y)
            newY = int(sin_deg * x + cos_deg * y)

            # Memindahkan koordinat agar gambar tidak terpotong
            newX += max_dim // 2
            newY += max_dim // 2

            # Pastikan koordinat berada dalam batas gambar output
            if 0 <= newX < max_dim and 0 <= newY < max_dim:
                outputImage[newY, newX] = image[y, x]

    return outputImage

# Membaca gambar
image = img.imread('D:\\Perkuliahan\\S5\\Pengolahan Citra Digital\\s6\\tiger.jpg')

# Rotasi gambar
rotated_image = rotateImage(image, 45)

# Menampilkan gambar asli dan gambar yang sudah diputar
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(rotated_image)
plt.axis('off')

plt.show()
