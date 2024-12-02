import numpy as np
import matplotlib.pyplot as plt
import imageio

# Load an image (grayscale) - Replace with the correct image path
image_array = imageio.imread('C:/Users/matil/OneDrive/Desktop PC Mati/uni/image.jpg', mode='F')

# Rest of the code remains the same
rows, cols = image_array.shape  
center_row, center_col = rows // 2, cols // 2  

radius = 50  
y, x = np.ogrid[:rows, :cols]  
mask = (x - center_col) ** 2 + (y - center_row) ** 2 <= radius ** 2  

fft_image = np.fft.fft2(image_array)
fft_image_shifted = np.fft.fftshift(fft_image)
fft_image_shifted[~mask] = 0  

magnitude_spectrum = np.log(np.abs(fft_image_shifted) + 1)  

plt.figure(figsize=(12, 6))  

plt.subplot(1, 2, 1)  
plt.imshow(image_array, cmap="gray")  
plt.title("Original Image")  
plt.axis("off")  

plt.subplot(1, 2, 2)  
plt.imshow(magnitude_spectrum, cmap="gray")  
plt.title("Masked Magnitude Spectrum")  
plt.axis("off")  

plt.show()
