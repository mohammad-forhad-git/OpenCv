import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() # Capture frame-by-frame, ret is a boolean indicating if the frame was read successfully,True/False
    
    if not ret:
        print("Failed to capture video")
        break
    cv2.imshow('Video Feed', frame) # Display the resulting frame   
    if cv2.waitKey(1) & 0xFF == ord('q'): # Press 'q' to quit
        break

cap.release() # Release the video capture object
cv2.destroyAllWindows()             