import cv2
import kociemba
import numpy as np
import time

cap = cv2.VideoCapture(0)

time.sleep(2.0)

while True:
    ret,frame = cap.read()

    image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
    image = cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel)
    image = cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel)

    image = cv2.adaptiveThreshold(gray,15,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.ADAPTIVE_THRESH_BINARY_INV,5,0)

    contours = cv2.findContours(image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)