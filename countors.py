import cv2 as cv


img = cv.imread('Resources/Photos/group 1.jpg')

cv.imshow("cats", img)
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow("grescales", gray)
canny = cv.Canny(gray,125,175)
cv.imshow("canny", canny)
# canny1 = cv.Canny(img, 125, 175)
# cv.imshow("img canny", canny1)

countours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

cv.waitKey(0)