#!/usr/bin/env python
import numpy as np
import cv2
import video

if __name__ == '__main__':
    import sys
    try: video_src = 'Samolet.mp4'#sys.argv[1]
    except: video_src = 0
    mser_delta=1
    mser_min_area=1 #prune the area which smaller than minArea
    mser_max_area=1000 #prune the area which bigger than maxArea
    mser_max_variation=10	 #prune the area have simliar size to its children
    mser_min_diversity=1000 #trace back to cut off mser with diversity < min_diversity

#The next few params for MSER of color image:
    mser_max_evolution=10 #for color image, the evolution steps
    mser_area_threshold=10 #the area threshold to cause re-initialize
    mser_min_margin=2 #ignore too small margin
    mser_edge_blur_size=10 #the aperture size for edge blur

    cam = video.create_capture(video_src)
    mser = cv2.MSER(mser_delta,mser_min_area,mser_max_area,mser_max_variation,mser_min_diversity,mser_max_evolution,mser_area_threshold,mser_min_margin,mser_edge_blur_size)
    idx=0
    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        vis = img.copy()
        
        regions = mser.detect(gray, None)
        hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
        cv2.polylines(vis, hulls, 1, (255, 0, 0))
        cv2.imshow('img', vis)
#	idx=idx+1
#	print("idx=",idx)
#	cv2.waitKey(10)
        if 0xFF & cv2.waitKey(5) == 27:
            break
    cv2.destroyAllWindows()
