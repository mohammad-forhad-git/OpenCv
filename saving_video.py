import cv2
camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID')
recorder = cv2.VideoWriter('my_video.avi', codec, 20.0, (frame_width, frame_height))

while True:
    sucess, frame = camera.read()
    if not sucess:
        print("Failed to capture video")
        break
    recorder.write(frame)
    cv2.imshow('Video Feed', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

recorder.release()
camera.release()
cv2.destroyAllWindows()