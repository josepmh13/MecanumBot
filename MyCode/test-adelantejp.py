import time
from roboclaw import Roboclaw

#Windows comport name
#rc = Roboclaw("COM3",115200)
#Linux comport name
Frontal = Roboclaw("/dev/ttyACM0",115200) #Para los motores frontales
Trasero = Roboclaw("/dev/ttyACM1",115200) #Para los motores traseros


Frontal.Open()
Trasero.Open()
address = 0x80

rep=0

while(rep<1):
	Frontal.ForwardM1(address,64)	#1/4 power forward
	Frontal.ForwardM2(address,64)	#1/4 power forward
	time.sleep(2)
	
	Frontal.ForwardBackwardM1(address,64)	#Stopped
	Frontal.ForwardBackwardM2(address,64)	#Stopped
	time.sleep(2)
	
	rep=rep+1
	

