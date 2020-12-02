from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.context_processors import request
from django.contrib.auth.models import User
from django.contrib import auth
import RPi.GPIO as GPIO #https://blender.pe.kr/593
from datetime import datetime
from django.utils import timezone
import time
import math
in1 = 24
in2 = 23
en = 25
      
GPIO.setmode(GPIO.BCM) 
GPIO.setup(in1,GPIO.OUT)    
GPIO.setup(in2,GPIO.OUT)    
GPIO.setup(en,GPIO.OUT)    
GPIO.output(in1,GPIO.LOW)    
GPIO.output(in2,GPIO.LOW)  
p=GPIO.PWM(en,1000)    
p.start(0)
     
    
def test(request) :
 
    p.ChangeDutyCycle(100)    
    #�닔
    if 'up' in request.POST:
        print("up")
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
              
    elif 'down' in request.POST:
        print("down")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
         
    elif 'stop' in request.POST:
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
  
    elif 'upRes' in request.POST : # time.sleep() �썑 stop   #�떒�쐞 蹂꾩씠�룞
        print("complete")
        global time
        x = int(request.POST.get('time'))
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        i = x*0.2
        time.sleep(int(i))
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
         
         
    elif 'downRes' in request.POST :
        print("complete")
        global time
        x = int(request.POST.get('time'))
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        i = x*0.2
        time.sleep(i)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
             
    elif 'off' in request.POST:
        GPIO.stop()
        GPIO.cleanup()
        print("GPIO Clean up")
  
    else :
        print("<<<  wrong data  >>>")
    return render(request,"test(re).html")