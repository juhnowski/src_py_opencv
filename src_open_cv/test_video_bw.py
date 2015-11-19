#!/usr/bin/python
import cv

capture = cv.CreateFileCapture('/home/ilya/src_open_cv/vsplesk.mp4')
cv.WaitKey(200)
frame=cv.QueryFrame(capture)
temp=cv.CloneImage(frame)
cv.Smooth(temp,temp,cv.CV_BLUR,5,5)
while True:
    frame=cv.QueryFrame(capture)
    cv.ShowImage("Window",frame)
    c=cv.WaitKey(40)
    if c==27: #Break if user enters 'Esc'.
        break
