from tkinter import *
from PIL import Image, ImageTk
import RPi.GPIO as GPIO
import time
import numpy as py
from threading import Thread
from queue import Queue
import csv
import sys
import random
import board
import busio
import adafruit_vl53l0x



pin_motorA=18 
pin_motorB=33

GPIO.setup(pin_motorA, GPIO.OUT)
pwm=GPIO.PWM(pin_motorA,50)

#GET VALUE OF t1 and t2 from 
M="2"
t1=0
t2=0
csv_file=csv.reader(open('zemax_distance.csv', "r"), delimiter=",")
for row in csv_file:
    if M==row[0]:
        print(row)
        distance_M=row
        t1=distance_M[1]
        t2=distance_M[2]
M=float(M)
t1=float(t1)
t2=float(t2)
print("DISTANCE WE ARE AIMING FOR", t1)
Top=t1+(t1*10/100)
print ("Top value acceptable",Top)
Bottom=t1-(t1*10/100)
print ("Bottom value acceptable", Bottom)
# print(t2)

i2c=busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)
pwm.start(0)
while True:
    d1_=0
    count=0
    average=10
    for count in range(average):
        d1=vl53.range
        d1_=d1_+d1
        count+=1
    Distance=(d1/count)*10
    print("Actual Distance", Distance)

    
    if Distance>Bottom and Distance<Top:
        print ("ok")
        break
    time.sleep(2)
    if Distance>Top:
        print("too far")
        pwm.ChangeDutyCycle(9)
        time.sleep(1)
   
    time.sleep(2)
    if Distance<Bottom:
        print("too close")
        pwm.ChangeDutyCycle(2)
        time.sleep(1)
    time.sleep(2)
        
    
pwm.stop()

GPIO.cleanup()
