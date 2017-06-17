# coding=utf-8
import math
import csv
import time
from roboclaw import Roboclaw

#Linux comport name
Frontal = Roboclaw("/dev/ttyACM0",115200) #Para los motores frontales
Trasero = Roboclaw("/dev/ttyACM1",115200) #Para los motores traseros
Frontal.Open()
Trasero.Open()
address = 0x80

### MOTOR1
def Motor1():
        Frontal.BackwardM1(address,25)

### MOTOR2
def Motor2():
        Frontal.ForwardM2(address,75)

### MOTOR3
def Motor3():
        Trasero.BackwardM1(address,25)

### MOTOR4
def Motor4():
        Trasero.ForwardM2(address,75)

### ADELANTE
def Adelante1x():
        Frontal.BackwardM1(address,25)
        Frontal.ForwardM2(address,25)
        Trasero.BackwardM1(address,25)
        Trasero.ForwardM2(address,25)

def Adelante2x():
        Frontal.BackwardM1(address,50)
        Frontal.ForwardM2(address,50)
        Trasero.BackwardM1(address,50)
        Trasero.ForwardM2(address,50)

def Adelante3x():
        Frontal.BackwardM1(address,75)
        Frontal.ForwardM2(address,75)
        Trasero.BackwardM1(address,75)
        Trasero.ForwardM2(address,75)

def Adelante4x():
        Frontal.BackwardM1(address,100)
        Frontal.ForwardM2(address,100)
        Trasero.BackwardM1(address,100)
        Trasero.ForwardM2(address,100)

def Adelante5x():
        Frontal.BackwardM1(address,125)
        Frontal.ForwardM2(address,125)
        Trasero.BackwardM1(address,125)
        Trasero.ForwardM2(address,125)

### REVERSE
def Atras1x():
        Frontal.ForwardM1(address,25)
        Frontal.BackwardM2(address,25)
        Trasero.ForwardM1(address,25)
        Trasero.BackwardM2(address,25)

def Atras2x():
        Frontal.ForwardM1(address,50)
        Frontal.BackwardM2(address,50)
        Trasero.ForwardM1(address,50)
        Trasero.BackwardM2(address,50)

def Atras3x():
        Frontal.ForwardM1(address,75)
        Frontal.BackwardM2(address,75)
        Trasero.ForwardM1(address,75)
        Trasero.BackwardM2(address,75)

def Atras4x():
        Frontal.ForwardM1(address,100)
        Frontal.BackwardM2(address,100)
        Trasero.ForwardM1(address,100)
        Trasero.BackwardM2(address,100)

def Atras5x():
        Frontal.ForwardM1(address,125)
        Frontal.BackwardM2(address,125)
        Trasero.ForwardM1(address,125)
        Trasero.BackwardM2(address,125)

# DETENERSE
def Detenerse():
        Frontal.ForwardM1(address,0)
        Frontal.ForwardM2(address,0)
        Trasero.ForwardM1(address,0)
        Trasero.ForwardM2(address,0)

### CCW TURN
def CCW1x():
        Frontal.ForwardM1(address,25)
        Frontal.ForwardM2(address,25)
        Trasero.ForwardM1(address,25) 
        Trasero.ForwardM2(address,25) 

def CCW2x():
        Frontal.ForwardM1(address,50)
        Frontal.ForwardM2(address,50)
        Trasero.ForwardM1(address,50)
        Trasero.ForwardM2(address,50)

def CCW3x():
        Frontal.ForwardM1(address,75)
        Frontal.ForwardM2(address,75)
        Trasero.ForwardM1(address,75)
        Trasero.ForwardM2(address,75)

def CCW4x():
        Frontal.ForwardM1(address,100)
        Frontal.ForwardM2(address,100)
        Trasero.ForwardM1(address,100)
        Trasero.ForwardM2(address,100)

def CCW5x():
        Frontal.ForwardM1(address,125)
        Frontal.ForwardM2(address,125)
        Trasero.ForwardM1(address,125)
        Trasero.ForwardM2(address,125)

### CW TURN
def CW1x():
        Frontal.BackardM1(address,25)
        Frontal.BackwardM2(address,25) 
        Trasero.BackwardM1(address,25)
        Trasero.BackwardM2(address,25) 

def CW2x():
        Frontal.BackwardM1(address,50)
        Frontal.BackwardM2(address,50)
        Trasero.BackwardM1(address,50)
        Trasero.BackwardM2(address,50)

def CW3x():
        Frontal.BackwardM1(address,75)
        Frontal.BackwardM2(address,75)
        Trasero.BackwardM1(address,75)
        Trasero.BackwardM2(address,75)

def CW4x():
        Frontal.BackwardM1(address,100)
        Frontal.BackwardM2(address,100)
        Trasero.BackwardM1(address,100)
        Trasero.BackwardM2(address,100)

def CW5x():
        Frontal.BackwardM1(address,125)
        Frontal.BackwardM2(address,125)
        Trasero.BackwardM1(address,125)
        Trasero.BackwardM2(address,125)

### RIGHT SHIFT
def RIGHT1x():
    Frontal.ForwardM1(address,25)
    Frontal.BackwardM2(address,25)
    Trasero.BackwardM1(address,25)
    Trasero.ForwardM2(address,25) 

def RIGHT2x():
    Frontal.ForwardM1(address,50)
    Frontal.BackwardM2(address,50)
    Trasero.BackwardM1(address,50)
    Trasero.ForwardM2(address,50)
	
def RIGHT3x():
    Frontal.ForwardM1(address,75)
    Frontal.BackwardM2(address,75)
    Trasero.BackwardM1(address,75)
    Trasero.ForwardM2(address,75)
	
def RIGHT4x():
    Frontal.ForwardM1(address,100)
    Frontal.BackwardM2(address,100)
    Trasero.BackwardM1(address,100)
    Trasero.ForwardM2(address,100)
	
def RIGHT5x():
    Frontal.ForwardM1(address,125)
    Frontal.BackwardM2(address,125)
    Trasero.BackwardM1(address,125)
    Trasero.ForwardM2(address,125)
        
### LEFT SHIFT
def LEFT1x():
    Frontal.BackwardM1(address,25)
    Frontal.ForwardM2(address,25)
    Trasero.ForwardM1(address,25)
    Trasero.BackwardM2(address,25)
      
def LEFT2x():
    Frontal.BackwardM1(address,50)
    Frontal.ForwardM2(address,50)
    Trasero.ForwardM1(address,50)
    Trasero.BackwardM2(address,50) 

def LEFT3x():
    Frontal.BackwardM1(address,75)
    Frontal.ForwardM2(address,75)
    Trasero.ForwardM1(address,75)
    Trasero.BackwardM2(address,75) 

def LEFT4x():
    Frontal.BackwardM1(address,100)
    Frontal.ForwardM2(address,100)
    Trasero.ForwardM1(address,100)
    Trasero.BackwardM2(address,100) 

def LEFT5x():
    Frontal.BackwardM1(address,125)
    Frontal.ForwardM2(address,125)
    Trasero.ForwardM1(address,125)
    Trasero.BackwardM2(address,125)
	
### N0 TURN
def NO1x():
    Frontal.ForwardM2(address,25)
    Trasero.ForwardM1(address,25) 

def NO2x():
    Frontal.ForwardM2(address,50)
    Trasero.ForwardM1(address,50)
	
def NO3x():
    Frontal.ForwardM2(address,75)
    Trasero.ForwardM1(address,75)
	
def NO4x():
    Frontal.ForwardM2(address,100)
    Trasero.ForwardM1(address,100)
	
def NO5x():
    Frontal.ForwardM2(address,125)
    Trasero.ForwardM1(address,125)
	
### SE TURN
def SE1x():
    Frontal.BackwardM2(address,25)
    Trasero.ForwardM1(address,25)
       
def SE2x():
    Frontal.BackwardM2(address,50)
    Trasero.ForwardM1(address,50) 

def SE3x():
    Frontal.BackwardM2(address,75)
    Trasero.ForwardM1(address,75) 

def SE4x():
    Frontal.BackwardM2(address,75)
    Trasero.ForwardM1(address,75)
	
def SE5x():
    Frontal.BackwardM2(address,125)
    Trasero.ForwardM1(address,125)
	
### NE TURN
def NE1x():
    Frontal.BackwardM1(address,25)
    Trasero.ForwardM2(address,25) 

def NE2x():
    Frontal.BackwardM1(address,50)
    Trasero.ForwardM2(address,50)
	
def NE3x():
    Frontal.BackwardM1(address,75)
    Trasero.ForwardM2(address,75)
	
def NE4x():
    Frontal.BackwardM1(address,100)
    Trasero.ForwardM2(address,100)
	
def NE5x():
    Frontal.BackwardM1(address,125)
    Trasero.ForwardM2(address,125)
     
### SO TURN
def SO1x():
    Frontal.BackwardM1(address,25)
    Trasero.BackwardM2(address,25)
	
def SO2x():
    Frontal.ForwardM1(address,50)
    Trasero.BackwardM2(address,50)
	
def SO3x():
    Frontal.ForwardM1(address,75)
    Trasero.BackwardM2(address,75)
	
def SO4x():
    Frontal.ForwardM1(address,100)
    Trasero.BackwardM2(address,100)
	
def SO5x():
    Frontal.ForwardM1(address,125)
    Trasero.BackwardM2(address,125)
         
def display_DV():
    encA = Frontal.ReadEncM1(address)
    encB = Frontal.ReadEncM2(address)
    encC = Trasero.ReadEncM1(address)
    encD = Trasero.ReadEncM2(address)
    speedA = Frontal.ReadSpeedM1(address)
    speedB = Frontal.ReadSpeedM2(address)
    speedC = Trasero.ReadSpeedM1(address)
    speedD = Trasero.ReadSpeedM2(address)
    print("EncoderA:"),
    if(encA[0]==1):
        print encA[1],
        #print format(encA[2],'02x'),
    else:
        print "failed",
    print "EncoderB:",
    if(encB[0]==1):
        print encB[1],
        #print format(encB[2],'02x'),
    else:
        print "failed " ,
    print("EncoderC:"),
    if(encC[0]==1):
        print encC[1],
        #print format(encC[2],'02x'),
    else:
        print "failed",
    print "EncoderD:",
    if(encD[0]==1):
        print encD[1],
        #print format(encD[2],'02x'),
    else:
        print "failed " ,
    print "SpeedA:",
    if(speedA[0]):
        print speedA[1],
    else:
        print "failed",
    print("SpeedB:"),
    if(speedB[0]):
        print speedB[1]
    else:
        print "failed "
    print "SpeedC:",
    if(speedC[0]):
        print speedC[1],
    else:
        print "failed",
    print("SpeedD:"),
    if(speedD[0]):
        print speedD[1]
    else:
        print "failed "
    return (encA[1], encB[1], encC[1], encD[1], speedA[1], speedB[1], speedC[1], speedD[1]) 

def EDV():
    r = 0.1015
    encA = Frontal.ReadEncM1(address)
    eA = encA[1]*2*r*math.pi/4800 
    encB = Frontal.ReadEncM2(address)
    eB = encB[1]*2*r*math.pi/4800
    encC = Trasero.ReadEncM1(address)
    eC = encC[1]*2*r*math.pi/4800
    encD = Trasero.ReadEncM2(address)
    eD = encD[1]*2*r*math.pi/4800
    speedA = Frontal.ReadSpeedM1(address)
    speedB = Frontal.ReadSpeedM2(address)
    speedC = Trasero.ReadSpeedM1(address)
    speedD = Trasero.ReadSpeedM2(address)
    #print("eA = ",eA," eB = ",eB," eC = ",eC," eD = ",eD)
    #return (eA, eB, eC, eD, speedA[1], speedB[1], speedC[1], speedD[1]) 
    print("encA = ",encA[1]," encB = ",encB[1]," encC = ",encC[1]," encD = ",encD[1])
    return (encA[1], encB[1], encC[1], encD[1], speedA[1], speedB[1], speedC[1], speedD[1])

def display_IP():
    iAB = Frontal.ReadCurrents(address)
    iCD = Trasero.ReadCurrents(address)
    pwmAB = Frontal.ReadPWMs(address)
    pwmCD = Trasero.ReadPWMs(address)
    return (float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2])

def writeCSV(writer,start,savelast):
    L1 = EDV()
    L2 = display_IP()
    writer.writerow([(-start+savelast), L1[0], L1[1], L1[2], L1[3], L1[4], L1[5], L1[6], L1[7], L2[0], L2[1], L2[2], L2[3], L2[4], L2[5], L2[6], L2[7]])
    time.sleep(0.01)

def displayspeed():
    speedA = Frontal.ReadSpeedM1(address)
    speedB = Frontal.ReadSpeedM2(address)
    speedC = Trasero.ReadSpeedM1(address)
    speedD = Trasero.ReadSpeedM2(address)
    print "SpeedA:",
    if(speedA[0]):
        print speedA[1],
    else:
        print "failed",
    print("SpeedB:"),
    if(speedB[0]):
        print speedB[1]
    else:
        print "failed "
    print "SpeedC:",
    if(speedC[0]):
        print speedC[1],
    else:
        print "failed",
    print("SpeedD:"),
    if(speedD[0]):
        print speedD[1]
    else:
        print "failed "
