# import cv2
# image = cv2.imread('python.png')
# if image is not None:
#     h, w, c = image.shape
#     print(f"Image Dimensions:\nwidth: {w}\nheight: {h}\nchannels: {c}")
# else:
#     print("Could not load image")    

import cv2
image = cv2.imread('python.png')
if image is not None:
    h,w,c = image.shape
    print(f"Image Dimensions:\nwidth: {w}\nheight: {h}\nchannels: {c}")
else:
    print("could not load image")    