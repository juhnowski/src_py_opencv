#!/usr/bin/env python
import numpy as np
import cv2
import video

if __name__ == '__main__':
    import sys
    try: video_src = '0_27_#1.MOV'#sys.argv[1]
    except: video_src = 0

    cam = video.create_capture(video_src)
    mser = cv2.MSER()
    idx=0
    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        vis = img.copy()
        if idx>0 and idx<200:
            regions = mser.detect(gray, None)
            hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
            cv2.polylines(vis, hulls, 1, (255, 0, 0))
        cv2.imshow('img', vis)
	idx=idx+1
	print("idx=",idx)
	cv2.waitKey(10)
        if 0xFF & cv2.waitKey(5) == 27:
            break
    cv2.destroyAllWindows()
