import cv2 as cv
import numpy as np


img = cv.imread('Resources/Photos/park.jpg')
cv.imshow("image", img)
#trasnlation 
def translation(img, x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat,dimensions)

#  -x == left
#  -y == up
#  x == right
#  y == down

# translated = translation(img,-100,100)
# cv.imshow("translated image", translated)

#ROTATION\

# def rotate(img,angle, rotpoint = None):
#     (height, width) = img.shape[:2]
#     if rotpoint is None:
#         rotpoint = (width//2, height//2)
#     rotMat = cv.getRotationMatrix2D(rotpoint, angle, 1.0)
#     dimension = (width,height)
#     return cv.warpAffine(img,rotMat, dimension)

# roatated = rotate(img, 45)
# cv.imshow("rotated image",roatated)


#resize
resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("resized",resize)

#fliping
flip = cv.flip(img, -1)
cv.imshow("flipped", flip)
cv.waitKey(0)
