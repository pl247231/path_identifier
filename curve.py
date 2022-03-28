import cv2 as cv
import numpy as np

img = cv.imread("/Users/local/PycharmProjects/curve/IMG_4812.jpg")
imgheight = img.shape[0]

slice_height = imgheight//3

slice1 = img[imgheight-slice_height:imgheight,]
slice2 = img[imgheight-2*slice_height:imgheight-slice_height,]
slice3 = img[imgheight-3*slice_height:imgheight-2*slice_height,]
cv.imshow("img", slice1)

cv.waitKey(0)

cv.imshow("img", slice2)

cv.waitKey(0)

cv.imshow("img", slice3)

cv.waitKey(0)
cv.destroyAllWindows()

