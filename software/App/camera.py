import cv2

# Initialize video capture (0 for default webcam)
cap = cv2.VideoCapture(0)

def capture(e):
# Check if camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
    else:
        # Capture a single frame
        ret, frame = cap.read()

        # Check if frame was captured successfully
        if ret:
            # Save the captured frame
            cv2.imwrite("img.jpg", frame)
            print("Image captured and saved as captured_image.jpg")
        else:
            print("Error: Could not read frame.")

    # Release the camera
    cap.release()
