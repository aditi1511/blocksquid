import eel
import cv2
from WaterClassifier import WaterType,FlowRateClassifier
VideoFile=cv2.VideoCapture("demovideo.mp4")
_,Background=VideoFile.read()
labels={0:'Fresh water',1:'Waste Water'}
eel.init('web')
@eel.expose
def my_python_method(param1,param2):
    print(param1+param2)
@eel.expose
def flowfeedback():
    framerates=[]
    watertypes=[]
    Frames=[]
    count=0
    while True:
        _,Frame=VideoFile.read()
        if _==False:
            break
        else:
            Frame=cv2.resize(Frame,(640,480))
            Frames.append(Frame)
            watertypes.append(WaterType(Frame,x=203,y=97,w=39,h=36))
            framerates.append(FlowRateClassifier(Frame,Background,x=203,y=97,w=39,h=36))
    #print(watertypes)
    CreditScore=round(10**(not(max(watertypes,key=watertypes.count))+1)*int(sum(framerates)/len(framerates))*0.0001,2)
    return(f"{labels[not(max(watertypes,key=watertypes.count))]}#{int(sum(framerates)/len(framerates))}#{CreditScore}")
            
eel.start('main.html',block=False)
#eel.my_javascript_function('Hello',' World')
while True:
    eel.sleep(1)

