import cv2
import numpy as np

VideoFile=cv2.VideoCapture("demovideo.mp4")
TotalFrames=[]
while True:
    _,Frame=VideoFile.read()
    if _==False:
        break
    Frame=cv2.resize(Frame,(640,480))
    gray=cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    ret,thresh2=cv2.threshold(Frame,127,255,cv2.THRESH_BINARY)
    print(f"Non zero: {cv2.countNonZero(thresh)}")
    #cv2.imshow("Thresh",np.hstack((cv2.cvtColor(thresh,cv2.COLOR_GRAY2BGR),Frame)))
    cv2.imshow("Thresholded Image",np.hstack((thresh2,Frame)))
    cv2.waitKey(1)
