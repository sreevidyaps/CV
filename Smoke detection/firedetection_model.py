import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.utils import to_categorical

training_data=[r"C:\Users\AMZ PC\OneDrive\Desktop\CV\Smoke detection\fire_dataset\fire_images", 
               r"C:\Users\AMZ PC\OneDrive\Desktop\CV\Smoke detection\fire_dataset\non_fire_images"]

def load_images(training_data):
    images = []
    labels = []
    for i in range(len(training_data)):
        folder = training_data[i]
        label = i  # 0 for fire, 1 for non-fire
        for filename in os.listdir(folder):
            try:
                img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)
                if img is not None:
                    # Resize image to 48x48 pixels
                    img = cv2.resize(img, (48, 48))
                    images.append(img)
                    labels.append(label)  # Correct label assignment
                else:
                    print(f"Warning: Failed to load {filename}")
            except Exception as e:
                print(f"Error: loading image {os.path.join(folder, filename)}: {e}")
    
    # Convert lists to numpy arrays
    images = np.array(images)
    labels = np.array(labels)

    # Debugging print statements to check data
    print(f"Total images loaded: {len(images)}")
    print(f"Images shape: {images.shape}")
    print(f"Labels shape: {labels.shape}")
    print(f"Sample labels: {labels[:10]}")  # Print first 10 labels for debugging

    return images, labels

# Load images and labels
images, labels = load_images(training_data)

# Further Debugging
print(f"Type of images array: {type(images)}")
print(f"Type of labels array: {type(labels)}")
print(f"First image shape: {images[0].shape}")  # Check shape of first image
