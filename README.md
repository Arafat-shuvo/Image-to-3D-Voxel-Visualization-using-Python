# Image to 3D Voxel Visualization using Python

A simple Python project that converts a 2D grayscale image into a **3D voxel representation** using OpenCV, NumPy, and Matplotlib.

The project demonstrates how pixel intensity values can be transformed into height values to generate a 3D voxel grid and visualize it using Matplotlib.

## Overview

This project follows a simple image-to-3D conversion pipeline:

1. Load an image in grayscale using OpenCV.
2. Resize the image to 50 × 50 pixels.
3. Normalize pixel intensity values between 0 and 1.
4. Convert normalized pixel values into height values.
5. Generate a 3D voxel grid using NumPy.
6. Visualize the voxel structure using Matplotlib.

## Technologies Used

- **Python** – Programming language
- **OpenCV** – Image loading and preprocessing
- **NumPy** – Numerical operations and voxel grid creation
- **Matplotlib** – 3D visualization

## Installation

Install the required libraries:

```bash
pip install opencv-python numpy matplotlib
```

## Project Workflow

### 1. Image Loading

Load the input image in grayscale mode using OpenCV.

### 2. Image Resizing

Resize the image to 50 × 50 pixels to simplify visualization and reduce computational requirements.

### 3. Normalization

Normalize pixel intensity values by dividing them by 255.

### 4. Height Map Generation

Convert normalized pixel intensities into integer height values ranging from 0 to 10.

### 5. Voxel Grid Creation

Create a 3D Boolean array with dimensions 50 × 50 × 10.

Each pixel determines the height of its corresponding voxel column.

### 6. 3D Visualization

Use Matplotlib's `ax.voxels()` function to visualize the generated 3D voxel structure.

## How to Run

1. Clone the repository.
2. Install the required dependencies.
3. Place your input image in the project directory.
4. Update the image path in the Python script.
5. Run the Python file.

```bash
python image_to_voxel.py
```

## Expected Output

The program generates a 3D voxel visualization based on the grayscale intensity of the input image.

- Brighter pixels produce taller voxel columns.
- Darker pixels produce shorter voxel columns.
- Black pixels produce no voxels.

## Learning Objectives

- Image processing with OpenCV
- NumPy array manipulation
- Grayscale image normalization
- Height map generation
- 3D voxel representation
- 3D visualization using Matplotlib

## Applications

- Basic 3D image representation
- Height map visualization
- Image-based 3D modeling concepts
- Computer Vision learning
- Understanding voxel-based representations

## Author

**Md. Arafat Hossain**

Research Assistant | Deep Learning | Computer Vision | Medical Image Analysis

GitHub: [@Arafat-shuvo](https://github.com/Arafat-shuvo)

---

⭐ If you find this project useful, consider giving it a star!
