import cv2 as cv
import numpy as np

img = cv.imread("/Users/local/PycharmProjects/curve/IMG_4812.jpg")
grayed = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
width = img.shape[0]
height = img.shape[1]
for y in range(height-1):
    check = False
    startx = 0
    for x in range(width-1):
        if (grayed[x][y] < 100 and check == False):
            startx = x
        elif(grayed[x][y] < 100 and check == True):
            cv.line(grayed, pt1=(startx, y), pt2=(x, y), color=0, thickness=3)
cv.imshow('hi', grayed)
cv.waitKey()

