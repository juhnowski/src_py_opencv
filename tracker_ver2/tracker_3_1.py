#!/usr/bin/env python
#http://opencvpython.blogspot.ru/2012/06/contours-2-brotherhood.html
import cv2
import video
import sys

if __name__ == '__main__':
    print __doc__

    try:
        fn = "/root/v/1.avi"
    except:
        fn = 0

    def nothing(*arg):
        pass

    cv2.namedWindow('edge')

    cap = video.create_capture(fn)
    mser = cv2.MSER()

    a0 = 0.0
    while True:
        flag, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thrs1 = 600
        thrs2 = 800
        edge = cv2.Canny(gray, thrs1, thrs2, apertureSize=5)
        vis = img.copy()
        vis /= 2
        vis[edge != 0] = (0, 255, 0)


        try:
           ret,thresh = cv2.threshold(gray,127,255,0)
           contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#           print len(contours)
           cv2.drawContours(edge,contours,-1,(0,255,0),3)
           cnt = contours[0]
           moments = cv2.moments(cnt)
           #area = moments['m00']
           area = cv2.contourArea(cnt)
           print area
           if area>a0:
              a0 = area
              print '====================================='
              print a0
              print '====================================='
#           print area
#           myFile.write(area)
#           print moments
        except:
             pass

        cv2.imshow('edge', edge)
        ch = cv2.waitKey(5)
        if ch == 27:
            break

    
    
    cv2.destroyAllWindows()

