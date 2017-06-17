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

    with open("csvMAX.csv", "wb") as f:
        writer = csv.writer(f,  delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(['Tiempo', 'EncA', 'EncB', 'EncC', 'EncD', 'vA', 'vB', 'vC', 'vD','iA','iB', 'iC', 'iD', 'pwmA', 'pwmB', 'pwmC', 'pwmD'])
        rep=0
        #try:
        while(rep<1):
            #while (Ein[0]<1 and Ein[1]<1 and Ein[2] <1 and Ein[3] <1):
            start = time.time()
            last = start
            while(time.time()-start< 2.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Adelante2x()
                    LM.writeCSV(start,savelast)

            print("\n--- %s seconds ---\n" % (time.time()-start))
            start = time.time()
            LM.Detenerse()
            time.sleep(2)
            print("\n--- %s seconds ---\n" % (time.time()-start))
            rep = rep + 1
        #except:
        #    print exceptions.AttributeError
        #    LM.Detenerse()

if __name__ == '__main__':
    main()
