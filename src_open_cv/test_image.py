#!/usr/bin/python
import cv
cv.NamedWindow('a_window',cv.CV_WINDOW_AUTOSIZE)
#image=cv.LoadImage('/home/ilya/src_open_cv/vsplesk.png',cv.CV_LOAD_IMAGE_COLOR)
g_capture = cv.CreateFileCapture('/home/ilya/src_open_cv/vsplesk.mp4')
image=cv.QueryFrame(g_capture)
font = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
x=10
y=50
cv.PutText(image,"x=0.0",(x,y),font,255)
cv.PutText(image,"y=0.0",(x,y+40),font,255)
cv.ShowImage('a_window', image)
cv.WaitKey(10000)

