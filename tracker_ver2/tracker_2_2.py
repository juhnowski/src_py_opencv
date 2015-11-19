#!/usr/bin/env python

'''
This sample demonstrates Canny edge detection.

Usage:
  edge.py [<video source>]

  Trackbars control edge thresholds.

'''

import cv2

# relative module
import video

# built-in module
import sys


if __name__ == '__main__':
    print __doc__

    try:
        fn = "/root/v/1.avi"#sys.argv[1]
    except:
        fn = 0

    def nothing(*arg):
        pass

    cv2.namedWindow('edge')
    #cv2.createTrackbar('thrs1', 'edge', 1600, 5000, nothing)
    #cv2.createTrackbar('thrs2', 'edge', 600, 5000, nothing)

    cap = video.create_capture(fn)
    while True:
        flag, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thrs1 = 500#cv2.getTrackbarPos('thrs1', 'edge')
        thrs2 = 4000#cv2.getTrackbarPos('thrs2', 'edge')
        edge = cv2.Canny(gray, thrs1, thrs2, apertureSize=5)
        vis = img.copy()
        vis /= 2
        vis[edge != 0] = (0, 255, 0)
        cv2.imshow('edge', vis)
        ch = cv2.waitKey(5)
        if ch == 27:
            break
    cv2.destroyAllWindows()

