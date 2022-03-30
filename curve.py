import cv2 as cv
import numpy as np

img = cv.imread("/Users/local/PycharmProjects/curve/IMG_4812.jpg")
grayed = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
height = img.shape[0]-1
width = img.shape[1]-1
slice_height = height//50
slice_width = width//50
midpoints = []
for j in range(50):
    y = height-j*slice_height
    check1 = False
    check2 = False
    for x in range(width):
        if(grayed[y,x] < 50):
            startx = x
            check1 = True
            break
    for x in range(width):
        if grayed[y,width-x] < 20:
            endx = width-x
            check2 = True
            break
    if(check1 and check2):
        mid = (startx+endx)//2
        midpoints.append((mid,y))
    else:
        ending = y
        break

cv.line(img, pt1 = (startx,1000), pt2 = (endx,1000), color = (0,0,0), thickness= 10)


cv.imshow('hi', img)
cv.waitKey()

