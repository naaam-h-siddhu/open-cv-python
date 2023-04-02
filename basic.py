import numpy as np
import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow("cat image",img)
#converting it in greyscale

# grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("cat greyscale", grey)

#making blurr image 
blurr = cv.GaussianBlur(img, (3,3) , cv.BORDER_DEFAULT)
# cv.imshow("blur cat", blurr)


#edge cascade

# canny = cv.Canny(img,125,175)
# cv.imshow("edge cascade", canny)

#dilating the image

# dilated = cv.dilate(canny,(7,7), iterations=1)
# cv.imshow("dilateed image of canny", dilated)

# #eroding the image

# eroded = cv.erode(dilated,(3,3),iterations=1)
# cv.imshow("eroded image", eroded)

#resize
# resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow("resized image", resize)

#cropping
croped = img[50:200, 100:213]
cv.imshow("Croped image", croped)
cv.waitKey(0)