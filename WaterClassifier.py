import pickle
import numpy as np
import cv2
labels={0:'Fresh water',1:'Waste Water'}
sumval=[0,0]
with open('datasetdictionary.pkl','rb') as f:  # Python 3: open(..., 'rb')
    data_dictionary = pickle.load(f)
FW=data_dictionary["Fresh"]
WW=data_dictionary["Polluted"]
def WaterType(frame,x=0,y=0,w=640,h=480):
    #x,y,w,h=cv2.selectROI(frame,False)
    frame=frame[y:y+h,x:x+w]
    imagec=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    imagehist = cv2.calcHist([imagec], [0, 1, 2], None, [8, 8, 8],[0, 256, 0, 256, 0, 256])
    imagehist = cv2.normalize(imagehist, imagehist).flatten()
    for i in FW:
        sumval[0]=sumval[0]+cv2.compareHist(imagehist, i, 0)
    for i in WW:
        sumval[1]=sumval[1]+cv2.compareHist(imagehist, i, 0)
    label_identified=sumval.index(max(sumval))
    return(labels[label_identified])
def FlowRateClassifier(frame,nm,x=0,y=0,w=640,h=480):
    subtraction=cv2.cvtColor(cv2.absdiff(frame[y:y+h,x:x+w],nm[y:y+h,x:x+w]),cv2.COLOR_BGR2GRAY)
    _,thresh11 = cv2.threshold(subtraction,20,255,cv2.THRESH_BINARY)
    #print(f"Pixel variation frame by frame: {cv2.countNonZero(thresh11)}sq pixels/s.")
    return(cv2.countNonZero(thresh11))
