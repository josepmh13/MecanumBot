# coding=utf-8
import csv
import time
import subprocess
import sys
import libmov as LM
from roboclaw import Roboclaw

#Linux comport name
Frontal = Roboclaw("/dev/ttyACM0",115200) #Para los motores frontales
Trasero = Roboclaw("/dev/ttyACM1",115200) #Para los motores traseros
Frontal.Open()
Trasero.Open()
address = 0x80


def main():

    Frontal.ResetEncoders(address)
    Trasero.ResetEncoders(address)
    time.sleep(1)
    ### TUNING PID
    Frontal.SetM1VelocityPID(6237.4408,1302.04466,0,6300)
    Frontal.SetM2VelocityPID(6237.4408,1302.04466,0,6300)
    Trasero.SetM1VelocityPID(6237.4408,1302.04466,0,6300)
    Trasero.SetM2VelocityPID(6237.4408,1302.04466,0,6300)

    #try:
    while(rep<1):
        Frontal.Speed1(-2000)
        Frontal.Speed2(2000)
        Trasero.Speed1(-2000)
        Trasero.Speed2(2000)
        LM.displayspeed()
        time.sleep(2)
        Frontal.Speed1(0)
        Frontal.Speed2(0)
        Trasero.Speed1(0)
        Trasero.Speed2(0)
        time.sleep(1)
        LM.Detenerse
        rep = rep + 1
    #except Exception as e:
    #   LM.Detenerse()

if __name__ == '__main__':
    main()
