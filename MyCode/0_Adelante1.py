import time
import serial
from roboclaw import Roboclaw

#Windows comport name
#rc = Roboclaw("COM3",115200)
#Linux comport name
Frontal = Roboclaw("/dev/ttyACM0",115200)
#Trasero = Roboclaw("/dev/ttyACM1",115200)

Frontal.Open()
#Trasero.Open()
address = 0x81
rep=0

while(rep<1):
        #adelante
        Frontal.ForwardM1(address,64)   #1/4 power forward
        Frontal.ForwardM2(address,64)   #1/4 power forward
  #      Trasero.ForwardM1(address,64)   #1/4 power forward
   #     Trasero.ForwardM2(address,64)   #1/4 power forward
        time.sleep(2)
        #para
        Frontal.ForwardBackwardM1(address,64)   #Stopped
        Frontal.ForwardBackwardM2(address,64)   #Stopped
    #    Trasero.ForwardBackwardM1(address,64)   #Stopped
     #   Trasero.ForwardBackwardM2(address,64)   #Stopped
        time.sleep(2)
        #atras
        Frontal.BackwardM1(address,64)  #1/4 power forward
        Frontal.BackwardM2(address,64)   #1/4 power forward
#       Trasero.BackwardM1(address,64)   #1/4 power forward
#       Trasero.BackwardM2(address,64)  #1/4 power forward
        time.sleep(2)
        #para
        Frontal.ForwardBackwardM1(address,64)   #Stopped
        Frontal.ForwardBackwardM2(address,64)   #Stopped
 #       Trasero.ForwardBackwardM1(address,64)   #Stopped
  #      Trasero.ForwardBackwardM2(address,64)   #Stopped
        time.sleep(2)
        #izquierda
        Frontal.ForwardM1(address,64)  #1/4 power forward
        Frontal.BackwardM2(address,64)   #1/4 power forward
   #     Trasero.BackwardM1(address,64)   #1/4 power forward
    #    Trasero.ForwardM2(address,64)  #1/4 power forward
        time.sleep(2)
        #para
        Frontal.ForwardBackwardM1(address,64)   #Stopped
        Frontal.ForwardBackwardM2(address,64)   #Stopped
        time.sleep(2)
        #izquierda
        Frontal.ForwardM1(address,64)  #1/4 power forward
        Frontal.BackwardM2(address,64)   #1/4 power forward
   #     Trasero.BackwardM1(address,64)   #1/4 power forward
    #    Trasero.ForwardM2(address,64)  #1/4 power forward
        time.sleep(2)
        #para
        Frontal.ForwardBackwardM1(address,64)   #Stopped
        Frontal.ForwardBackwardM2(address,64)   #Stopped
        Frontal.ForwardBackwardM1(address,64)   #Stopped
        Frontal.ForwardBackwardM2(address,64)   #Stopped
 #       Trasero.ForwardBackwardM1(address,64)   #Stopped
 #       Trasero.ForwardBackwardM2(address,64)   #Stopped
        time.sleep(2)

        rep=rep+1
