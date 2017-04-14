# coding=utf-8
import csv
import time
import subprocess
import time
#import serial
from roboclaw import Roboclaw

#Linux comport name
Frontal = Roboclaw("/dev/ttyACM0",115200) #Para los motores frontales
Trasero = Roboclaw("/dev/ttyACM1",115200) #Para los motores traseros
Frontal.Open()
Trasero.Open()
address = 0x80

def Adelante():
        Frontal.ForwardM1(address,64)   #1/4 power forward
        Frontal.ForwardM2(address,64)   #1/4 power forward
        Trasero.ForwardM1(address,64)   #1/4 power forward
        Trasero.ForwardM2(address,64)   #1/4 power forward

def Atras():
        Frontal.BackwardM1(address,64)   #1/4 power backward
        Frontal.BackwardM2(address,64)   #1/4 power backward
        Trasero.BackwardM1(address,64)   #1/4 power backward
        Trasero.BackwardM2(address,64)   #1/4 power backward

def Detenerse():
        Frontal.ForwardBackwardM1(address,64)   #Stopped
        Frontal.ForwardBackwardM2(address,64)   #Stopped
        Trasero.ForwardBackwardM1(address,64)   #Stopped
        Trasero.ForwardBackwardM2(address,64)   #Stopped

def displayspeed():

        #Frontal.ResetEncoders(address)
        #Trasero.ResetEncoders(address)
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

        return (encA[1], encB[1], encC[1], encD[1])


def main():

    Frontal.ResetEncoders(address)
    Trasero.ResetEncoders(address)

    with open("csvFile.csv", "wb") as f:
        writer = csv.writer(f,  delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(['Tiempo', 'EncA', 'EncB', 'EncC', 'EncD', 'iA','iB', 'iC', 'iD'])

        rep=0
        while(rep<1):

            start_time = time.time()
            ee = displayspeed()
            Ein = list()
            Ein[0] = abs(ee[0])
            Ein[1] = abs(ee[1])
            Ein[2] = abs(ee[2])
            Ein[3] = abs(ee[3])

            while (Ein[0]<4800 and Ein[1]<4800 and Ein[2]<4800 and Ein[3]<4800):
                Atras()
                #for i in range(0,150):
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100])
                time.sleep(0.01)
                Ein = abs(lectura[1])

            print("\n--- %s seconds ---\n" % (time.time() - start_time))
            start_time = time.time()
            Detenerse()
            time.sleep(2)
            print("\n--- %s seconds ---\n" % (time.time() - start_time))
            #writer.writerow(['Tiempo', 'EncA', 'EncB', 'EncC', 'EncD', 'iA','iB', 'iC', 'iD'])
            #writer.writerow(['Tiempo', lectura[0], lectura[1], lectura[2], lectura[3],'iA','iB', 'iC', 'iD'])
            rep = rep + 1
            #### LAZO PARA GUARDAR LOS DATOS RECOPILADOS!!!!

if __name__ == '__main__':
    main()
