import cv2

image = cv2.imread('python.png')
if image is not None:
    print("Image Loaded")
    
    resize = cv2.resize(image,(300,300))
    
    cv2.imshow('Original Image', image)
    cv2.imshow('Resized Image', resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()