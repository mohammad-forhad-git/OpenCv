    

import cv2

image = cv2.imread('python.png')

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    cv2.imshow('grayscale image display',gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Could not find image')    
    