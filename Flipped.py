import cv2

image = cv2.imread('python.png')
if image is not None:
    print("Image Loaded")
    
    flipped_horizontal = cv2.flip(image, 1)
    flipped_vertical = cv2.flip(image, 0)
    flipped_both = cv2.flip(image, -1)
    
    cv2.imshow('Original Image', image)
    cv2.imshow('Flipped Horizontally', flipped_horizontal)
    cv2.imshow('Flipped Vertically', flipped_vertical)
    cv2.imshow('Flipped Both', flipped_both)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()