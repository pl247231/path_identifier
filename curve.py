import cv2 as cv

img = cv.imread("/Users/local/PycharmProjects/curve/IMG-4839.jpg")
grayed = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
height = img.shape[0]-1
width = img.shape[1]-1
slice_height = height//15

midpoints = []
thresh = 60
im_bw = cv.threshold(grayed, thresh, 255, cv.THRESH_BINARY)[1]
cv.imshow("img", im_bw)
cv.waitKey()
for j in range(14):
    y = height-j*slice_height
    check1 = False
    check2 = False

    for x in range(2*width//3):
        if(im_bw[y,x] < 40):
            startx = x
            check1 = True
            break
    for x in range(2*width//3):
        if im_bw[y,width-x] < 40:
            endx = width-x
            check2 = True
            break
    if(check1 and check2):
        mid = (startx+endx)//2
        midpoints.append((mid,y))
    else:
        ending = y
        break


second_x = midpoints[-1][0]
slope = (midpoints[-1][1]-midpoints[-2][1])/(midpoints[-1][0]- midpoints[-2][0])
if(slope < 0):
    slice_width = (width - midpoints[-1][0]) // 10
    for i in range(2, 10):
        x = second_x + slice_width * (i + 1)
        check1 = False
        check2 = False
        for y in range(height):
            if (im_bw[y, x] < 40):
                starty = y
                check1 = True
                break
        for y in range(height):
            if (im_bw[height - y, x] < 40):
                endy = height - y
                check2 = True
                break
        if (check1 and check2):
            mid = (starty + endy) // 2
            midpoints.append((x, mid))
else:
    slice_width = midpoints[-1][0]// 10
    for i in range(2, 10):
        x = second_x - slice_width * (i + 1)
        check1 = False
        check2 = False
        for y in range(height):
            if (im_bw[y, x] < 40):
                starty = y
                check1 = True
                break
        for y in range(height):
            if (im_bw[height - y, x] < 40):
                endy = height - y
                check2 = True
                break
        if (check1 and check2):
            mid = (starty + endy) // 2
            midpoints.append((x, mid))
for i in range(len(midpoints) - 1):
    cv.arrowedLine(img = img, pt1 = midpoints[i], pt2 = midpoints[i+1], thickness = 5, color = (0,255 ,0))


cv.imshow('hi', img)
cv.waitKey()
