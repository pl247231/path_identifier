import cv2 as cv
import numpy as np

img = cv.imread("/Users/local/PycharmProjects/curve/IMG-4812.jpg")
grayed = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
height = img.shape[0]-1
width = img.shape[1]-1
slice_height = height//20

midpoints = []

for j in range(20):
    y = height-j*slice_height
    check1 = False
    check2 = False

    for x in range(width):
        if(grayed[y,x] < 15):
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

slice_width = (width - midpoints[-1][0])//15
second_x = midpoints[-1][0]
for i in range(14):
    x = second_x + slice_width*(i+1)
    check1 = False
    check2 = False
    for y in range(height):
        if(grayed[y,x] < 50):
            starty = y
            check1 = True
            break
    for y in range(height):
        if(grayed[height-y,x] < 50):
            endy = height-y
            check2 = True
            break
    if (check1 and check2):
        mid = (starty + endy) // 2
        midpoints.append((x, mid))
for i in range(len(midpoints) - 1):
    cv.arrowedLine(img = img, pt1 = midpoints[i], pt2 = midpoints[i+1], thickness = 5, color = (0,255 ,0))


cv.imshow('hi', img)
cv.waitKey()

