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
    Frontal.SetM1VelocityPID(address,6237.4408,-1302.04466,0,6300)
    Frontal.SetM2VelocityPID(address,6237.4408,1302.04466,0,6300)
    Trasero.SetM1VelocityPID(address,6237.4408,-1302.04466,0,6300)
    Trasero.SetM2VelocityPID(address,6237.4408,1302.04466,0,6300)
    rep = 0;
    #try:
    while(rep<1):
        Frontal.SpeedM1(address,3300)
        Frontal.SpeedM2(address,3300)
        Trasero.SpeedM1(address,3300)
        Trasero.SpeedM2(address,3300)
        LM.displayspeed()
        time.sleep(3)
        Frontal.SpeedM1(address,0)
        Frontal.SpeedM2(address,0)
        Trasero.SpeedM1(address,0)
        Trasero.SpeedM2(address,0)
        time.sleep(1)
        LM.Detenerse
        rep = rep + 1
    #except Exception as e:
    #   LM.Detenerse()

if __name__ == '__main__':
    main()
