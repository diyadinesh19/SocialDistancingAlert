import cv2
#from vidgear.gears import CamGear
import pafy
from flask import Flask, redirect, url_for, request, render_template


import youtube_dl

width = int(input("What is the width in ft(nearest whole number)?"))
height = int(input("What is the length in ft(nearest whole number)?"))
#url = "https://youtu.be/VYsHV7WPyFw"
#videoPafy = pafy.new(url)
#best = videoPafy.getbest(preftype="webm")

fullCascade= cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_fullbody.xml")
upCascade= cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_upperbody.xml")
lowCascade= cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_lowerbody.xml")
faceCascade= cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture("Test.mov")#play.url)
#cap = cv2.VideoCapture(best.url)
#cap = CamGear(source='https://youtu.be/VYsHV7WPyFw', y_tube=True).start()
#totalArea*=1152
cap.set(3, 300) #width id is three
cap.set(4, 300) #height id is four
cap.set(10, 100) #brightness id is 10
socialDistance = True
while True:
    success, img = cap.read()
    #if not success:
       # break
    # print(img.shape)
    origImg = img
    # img = img[3*len(img)//4:,100:200]#[:50]
    # origImg = img
    img = cv2.resize(img, (width, height))
    sixFeet = 6  # img.shape[0] * img.shape[1] * 6 // (totalArea)  # 6912#**(1/2))
    #print(img.shape)
    # img = cv2.imread('Resources/lena.png')
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fulls = fullCascade.detectMultiScale(imgGray, 1.1, 4)
    ups = upCascade.detectMultiScale(imgGray, 1.1, 4)
    lows = lowCascade.detectMultiScale(imgGray, 1.1, 4)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    fullCount = 0
    upsCount = 0
    lowsCount = 0
    faceCount = 0
    """for (x,y,w,h) in fulls:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        fullCount+=1
        for (x1,y1,w1,h1) in fulls:
            dist = int(((x - x1) ** 2 + (y - y1) ** 2) * (1 / 2))
            diffx = abs(x1 - x)
            diffy = abs(y1 - y)
            if not ((sixFeet - 20) <= dist <= (sixFeet + 20)) and not (diffx < 10 and diffy < 10):
                print("THANKS!")
            else:
                print("PLEASE MAINTAIN SOCIAL DISTANCING!!!")
    for (x,y,w,h) in ups:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        upsCount+=1
        for (x1,y1,w1,h1) in ups:
            dist = int(((x-x1)**2+(y-y1)**2)*(1/2))
            diffx = abs(x1-x)
            diffy = abs(y1-y)
            if not ((sixFeet-20) <= dist <= (sixFeet+20)) and not(diffx<10 and diffy<10):
                print("THANKS!")
            else:
                print("PLEASE MAINTAIN SOCIAL DISTANCING!!!")"""
    socialDistance = True
    for (x, y, w, h) in ups:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        upsCount += 1
        for (x1, y1, w1, h1) in ups:
            dist = int(((x - x1) ** 2 + (y - y1) ** 2) * (1 / 2))
            diffx = abs(x1 - x)
            diffy = abs(y1 - y)
            if not ((dist>=sixFeet-3)) and not (diffx < 10 and diffy < 10):
                socialDistance = socialDistance
            else:
                socialDistance = False
    if socialDistance:
        print("Thank you for following Social Distancing")
    else:
        print("Please Maintain Social Distancing")
    #lowsCount = lowsCount-fullCount if lowsCount-fullCount >0 else 0
    #upsCount = upsCount - fullCount if upsCount - fullCount > 0 else 0
    #faceCount = faceCount - fullCount if faceCount - fullCount > 0 else 0
    totalCount = upsCount  # fullCount + lowsCount + upsCount # faceCount
    print(totalCount)
    cv2.waitKey(1)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0XFF == ord("q"):
        break
