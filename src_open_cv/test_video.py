#!/usr/bin/python
import cv

cv.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)

#SET CAMERA INDEX BELOW
camera_index = -1 

capture = cv.CreateFileCapture('vsplesk.mp4')
isRunning = True
image = cv.QueryFrame(capture)

def repeat():
  global capture #declare as globals since we are assigning to them now
  global camera_index
  global isRunning
  global firstImage
  c = cv.WaitKey(10) % 0x10
#  currImage = cv.QueryFrame(capture) 
	dst_16s2 = cv.CreateImage(cv.GetSize(image), cv.IPL_DEPTH_16S, 1)
	cv.Laplace(image, dst_16s2,3)
	cv.Convert(dst_16s2,image)
  cv.ShowImage("w1",image)

  if(c==27):
    isRunning = False

while isRunning:
    repeat()
