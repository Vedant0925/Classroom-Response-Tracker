import cv2

# Access the camera feed
camera = cv2.VideoCapture(0)
_, image = camera.read()

# Alternatively, load an image file
image = cv2.imread('classroom_image.jpg')

# Release the camera if used
camera.release()
