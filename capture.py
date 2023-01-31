import cv2

def capture():
    # Open the camera
    cap = cv2.VideoCapture(0)

    # Read the frame
    ret, frame = cap.read()

    # Save the image
    cv2.imwrite("trash.jpg", frame)

    # Release the camera
    cap.release()
