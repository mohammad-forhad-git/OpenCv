import cv2
image = cv2.imread('python.png')

if image is not None:
    cropped = image[200:400, 50:150]
    
    cv2.imshow("Original image", image)
    cv2.imshow("Cropped image", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()