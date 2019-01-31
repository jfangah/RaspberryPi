# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO  
import time  
  
#初始化  
def init():  
    #设置不显示警告  
    GPIO.setwarnings(False)  
    #设置读取面板针脚模式  
    GPIO.setmode(GPIO.BOARD)  
    #设置读取针脚标号  
    GPIO.setup(16,GPIO.IN)  
    pass  
   
def detct():  
    while True:   
        #当高电平信号输入时报警  
        if GPIO.input(16) == True:  
            #alart(curtime)  
            print('hello world')
        else:  
            continue  
        time.sleep(3)  
  
    0    
 
time.sleep(2)  
  
init()  
detct()  
GPIO.cleanup()  