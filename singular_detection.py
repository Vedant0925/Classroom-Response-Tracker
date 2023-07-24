import cv2
from PIL import Image
import numpy as np
import time


image_path = "path name"


pil_image = Image.open(image_path)


image = np.array(pil_image)


if image is None:
    print("Error: Unable to load the image from the specified file path.")
else:
    print("Image loaded successfully.")

# Resize the image to a smaller resolution
resized_image = cv2.resize(image, (800, 600))  # Adjust the size as needed

# Convert the resized image to grayscale
gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the grayscale image
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Threshold the blurred image to get a binary image
thresholded = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)[1]

# Find contours in the binary image
contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Fine-tune these parameters based on your image characteristics and speed requirements
min_contour_area = 1000
aspect_ratio_range = (1.2, 1.8)

# Filter potential placards based on size and aspect ratio
potential_placards = []
for contour in contours:
    area = cv2.contourArea(contour)
    x, y, w, h = cv2.boundingRect(contour)
    aspect_ratio = w / float(h)

    if area > min_contour_area and aspect_ratio_range[0] < aspect_ratio < aspect_ratio_range[1]:
        potential_placards.append(contour)

# Assuming there is only one detected placard, get its bounding rectangle
if len(potential_placards) == 1:
    x, y, w, h = cv2.boundingRect(potential_placards[0])

    # Calculate the center point of the placard
    center_x = x + w // 2
    center_y = y + h // 2

    # Determine the response based on the placard's position
    response = None
    if center_x < resized_image.shape[1] // 2 and center_y < resized_image.shape[0] // 2:
        response = 'A'
    elif center_x >= resized_image.shape[1] // 2 and center_y < resized_image.shape[0] // 2:
        response = 'B'
    elif center_x < resized_image.shape[1] // 2 and center_y >= resized_image.shape[0] // 2:
        response = 'C'
    else:
        response = 'D'

   
    cv2.putText(resized_image, f"Response: {response}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Response Mapping", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: No or multiple placards detected in the image.")


start_time = time.time()

end_time = time.time()
print("Execution time:", end_time - start_time)
