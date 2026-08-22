import cv2
import numpy as np
import matplotlib.pyplot as plt

# Image Load (Grayscale)
img = cv2.imread(
    r"C:\Users\Arafat\Desktop\Python Basic\images.jpg",
    cv2.IMREAD_GRAYSCALE
)
# ছোট করে নেওয়া (visualization সহজ করার জন্য)
img = cv2.resize(img, (50, 50))

# Normalize
img = img / 255.0

# Height Map তৈরি
height = (img * 10).astype(int)

# Voxel Grid
voxels = np.zeros((50, 50, 10), dtype=bool)

for x in range(50):
    for y in range(50):
        h = height[x, y]

        if h > 0:
            voxels[x, y, :h] = True

# 3D Plot
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

ax.voxels(voxels)

plt.title("Image to Voxel")
plt.show()