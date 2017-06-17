# coding=utf-8
import csv
import time
import subprocess
import libmov as LM
#import serial
from roboclaw import Roboclaw

#Linux comport name
Frontal = Roboclaw("/dev/ttyACM0",115200) #Para los motores frontales
Trasero = Roboclaw("/dev/ttyACM1",115200) #Para los motores traseros
Frontal.Open()
Trasero.Open()
address = 0x80

def displayspeed():

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


def main():

    Frontal.ResetEncoders(address)
    Trasero.ResetEncoders(address)
    time.sleep(2)

    with open("csvDEAD.csv", "wb") as f:
        writer = csv.writer(f,  delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(['Tiempo', 'EncA', 'EncB', 'EncC', 'EncD', 'vA', 'vB', 'vC', 'vD','iA','iB', 'iC', 'iD', 'pwmA', 'pwmB', 'pwmC', 'pwmD'])

        rep=0
        while(rep<1):

            start_time = time.time()
            ee = displayspeed()
            Ein = [abs(ee[0]), abs(ee[1]), abs(ee[2]), abs(ee[3])]
            dead = 0;
            while(Ein[0]<20 and Ein[1]<20 and Ein[2]<20 and Ein[3]<20):
                Frontal.BackwardM1(address,dead)
                Frontal.BackwardM2(address,dead)
                Trasero.BackwardM1(address,dead)
                Trasero.BackwardM2(address,dead)
                lectura = displayspeed()
                Ein =[abs(lectura[0]), abs(lectura[1]), abs(lectura[2]), abs(lectura[3])]
                time.sleep(1)
                print(dead)
                dead = dead + 1
           
            time.sleep(2)
            print('---\n Banda Muerta:\n ---')
            print(dead)
            Frontal.ForwardM1(address,0)
            Frontal.ForwardM2(address,0)
            Trasero.ForwardM1(address,0)
            Trasero.ForwardM2(address,0)
             
            rep = rep + 1

if __name__ == '__main__':
    main()

