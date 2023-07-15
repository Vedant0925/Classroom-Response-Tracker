# Iterate over the potential placards and map responses
for placard in potential_placards:
    # Get the bounding rectangle coordinates of the placard
    x, y, w, h = cv2.boundingRect(placard)

    # Calculate the center point of the placard
    center_x = x + w // 2
    center_y = y + h // 2

    # Perform response mapping based on the placard's position
    if center_x < image.shape[1] // 2 and center_y < image.shape[0] // 2:
        # Student in the top-left quadrant, response A
        response = 'A'
    elif center_x >= image.shape[1] // 2 and center_y < image.shape[0] // 2:
        # Student in the top-right quadrant, response B
        response = 'B'
    elif center_x < image.shape[1] // 2 and center_y >= image.shape[0] // 2:
        # Student in the bottom-left quadrant, response C
        response = 'C'
    else:
        # Student in the bottom-right quadrant, response D
        response = 'D'

    # Print the mapped response
    print("Mapped response:", response)
