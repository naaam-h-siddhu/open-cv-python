import cv2 as cv
import numpy as np 

blank = np.zeros((500,500, 3), dtype = 'uint8')
cv.imshow('Blank', blank)
# 1. Paint the image at certain colour
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('REd', blank)

# 2. Draw a Rectangle
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness = -1)
# cv.imshow('rectangle', blank)

#3. Draw a Circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness = -1)
# cv.imshow('With circle', blank)

#4. draw a line
# cv.line(blank, (100,0), (blank.shape[1]//2, blank.shape[1]//2),(255,255,255))
# cv.imshow("with line", blank)

#5. write text on the blank image
cv.putText(blank, "hello", (0,255), cv.FONT_HERSHEY_TRIPLEX,1.0, (0,255,0),2)
cv.imshow("text on image", blank)
cv. waitKey(0)
