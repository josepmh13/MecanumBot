# coding=utf-8
import time
import subprocess
#import serial
from roboclaw import Roboclaw
import libmov as LM

Frontal = Roboclaw("/dev/ttyACM0",115200) #Para los motores frontales
Trasero = Roboclaw("/dev/ttyACM1",115200) #Para los motores traseros
Frontal.Open()
Trasero.Open()
address = 0x80

def main():
	time.sleep(1)
	LM.Adelante2x()
	time.sleep(2)
	LM.Detenerse()
	time.sleep(1)	
	LM.Atras2x()
	time.sleep(2)
	LM.Detenerse()
	time.sleep(1)
	LM.RIGHT3x()
	time.sleep(2)
	LM.Detenerse()
	time.sleep(1)
	LM.LEFT3x()
	time.sleep(2)
	LM.Detenerse()
	time.sleep(1)
	LM.SE3x()
	time.sleep(2)
	LM.Detenerse()
	time.sleep(1)
	LM.NO3x()
	time.sleep(2)
	LM.Detenerse()
	time.sleep(1)
	LM.SO3x()
	time.sleep(2)
	LM.Detenerse()
	time.sleep(1)
	LM.NE3x()
	time.sleep(2)
	LM.Detenerse()
	time.sleep(1)
	LM.CCW5x()
	time.sleep(3)
	LM.Detenerse()
	time.sleep(1)
	LM.CW5x()
	time.sleep(3)
	LM.Detenerse()
	time.sleep(1)
	
	

if __name__ == '__main__':
    main()

