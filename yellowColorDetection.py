import cv2
import numpy as np
from PIL import Image
def detect_yellow_color():
    # Open a video feed (0 for the default camera)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Define the lower and upper bounds for yellow in the HSV color space
    lower_yellow = np.array([20, 100, 100])  # Adjust as needed
    upper_yellow = np.array([30, 255, 255]) # Adjust as needed

    while True:
        # Read a frame from the video feed
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Convert the frame to HSV color space
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create a mask for detecting yellow color
        mask = cv2.inRange(hsv_frame, lower_yellow, upper_yellow)

        mask_=Image.fromarray(mask)
        # Apply the mask to the original frame
        bbox=mask_.getbbox()
        if bbox is not None:
            x1,y1,x2,y2=bbox
            frame=cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),5)
            cv2.imshow("Original Frame", frame)
   

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video feed and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_yellow_color()
