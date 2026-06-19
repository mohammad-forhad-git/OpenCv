import cv2
image = cv2.imread('python.png')

if image is not None:
    success = cv2.imwrite('output_python.png',image)
    if success:
        print("Image saved successfully")
    else:
        print("Failed to save image")
else:
    print("Error: could not load image")        
    
    
