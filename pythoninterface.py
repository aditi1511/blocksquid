import eel
import cv2
VideoFile=cv2.VideoCapture("demovideo.mp4")
eel.init('web')
@eel.expose
def my_python_method(param1,param2):
    print(param1+param2)
@eel.expose
def flowfeedback():
    _,Frame=VideoFile.read()
    if _==False:
        return("False")
    Frame=cv2.resize(Frame,(640,480))
    gray=cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    return(cv2.countNonZero(thresh))
    #cv2.imshow("Thresh",thresh)
eel.start('main.html',block=False)
#eel.my_javascript_function('Hello',' World')
while True:
    eel.sleep(1)

