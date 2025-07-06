import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
        # Optional: Perform operations on the frame (e.g., convert to grayscale)
        # gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Live Feed', frame) # Display the frame
        # cv2.imshow('Grayscale Feed', gray_frame) # Display processed frame

    if cv2.waitKey(1) & 0xFF == ord('q'): # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()
