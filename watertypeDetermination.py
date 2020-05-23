#This code is just to map hsv values and see what type of water is present based on it's color properties
import cv2
import numpy as np
import glob
import pickle
#fresh_water_path=r'path_to_fresh_water_dataset'
fresh_water_path=r'G:\Fight_Corona\Blockchain\videoProcessingJS\pjsinterface\freshwater'
#waste_water_path=r'path_to_image_waste_water_dataset'
waste_water_path=r'G:\Fight_Corona\Blockchain\videoProcessingJS\pjsinterface\wastewater'
imageHtokenForFreshwater=[]
imageHtokenForWasteWater=[]
for imagePath in glob.glob(fresh_water_path + "/*.jpg"):
    filename = imagePath[imagePath.rfind("/") + 1:]
    image = cv2.imread(imagePath)
    imageH=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    imageH = cv2.calcHist([imageH], [0, 1, 2], None, [8, 8, 8],[0, 256, 0, 256, 0, 256])
    imageH = cv2.normalize(imageH, imageH).flatten()
    imageHtokenForFreshwater.append(imageH)
for imagePath in glob.glob(waste_water_path + "/*.jpg"):
    filename = imagePath[imagePath.rfind("/") + 1:]
    image = cv2.imread(imagePath)
    imageH=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    imageH = cv2.calcHist([imageH], [0, 1, 2], None, [8, 8, 8],[0, 256, 0, 256, 0, 256])
    imageH = cv2.normalize(imageH, imageH).flatten()
    imageHtokenForWasteWater.append(imageH)

datasetdictionary={"Fresh":imageHtokenForFreshwater,"Polluted":imageHtokenForWasteWater}

with open('datasetdictionary.pkl', 'wb') as f:
    pickle.dump(datasetdictionary, f)

