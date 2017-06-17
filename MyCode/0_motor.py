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
    with open("csvFile5.csv", "wb") as f:
        writer = csv.writer(f,  delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(['Tiempo', 'EncA', 'EncB', 'EncC', 'EncD','vA', 'vB', 'vC', 'vD', 'iA','iB', 'iC', 'iD', 'pwmA', 'pwmB', 'pwmC', 'pwmD'])

        rep=0
        while(rep<1):

            start_time = time.time()
	    #ADELANTE1X POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Adelante1x()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE ADELANTE 1X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))
            
	    #ADELANTE2X POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Adelante2x()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE ADELANTE 2X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))
             
            #ADELANTE3x POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Adelante3x()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE ADELANTE 3X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start)) 
            
            #ADELANTE4X POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Adelante4x()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE ADELANTE 4X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))
 
            #ADELANTE5X POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Adelante5x()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE ADELANTE 5X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))
            
            #ADELANTE4X POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Adelante4x()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE ADELANTE 4X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))


            #ADELANTE3X POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Adelante3x()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE ADELANTE 3X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))
  
            #ADELANTE2X POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Adelante2x()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE ADELANTE 2X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))            
 
            #ADELANTE1X POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Adelante1x()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE ADELANTE 1X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))
            
            #DETENERSE POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Detenerse()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE DETENERSE ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

            #ATRAS1X POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Atras1x()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6],lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE ATRAS 1X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))
            
            #ATRAS2X POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Atras2x()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE ATRAS 2X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))
            
            #ATARS3X POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Atras3x()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE ATRAS 3X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))
            
            #ATRAS4X POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Atras4x()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE ATRAS 4X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))
            
            #ATRAS5X POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Atras5x()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE ATRAS 5X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))
            
            #ATRAS4X POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Atras4x()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE ATRAS 4X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))
            
            #ATRAS3X POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Atras3x()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE ATRAS 3X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))
   
            #ATARS2X POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Atras2x()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE ATRAS 2X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))
            
            #ATRAS1X POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Atras1x()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE ATRAS 1X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

	    ###DETENERSE 3 SEGUNDOS
            start = time.time()
            while(time.time()-start < 3.0):
                LM.Detenerse()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE DETENERSE ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))
            
            #ADELANTE2X POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Adelante2x()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE ADELANTE 2X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))
            
            #ATRAS2X POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Atras2x()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE ATRAS 2X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))
            
            #DETENERSE POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Detenerse()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE DETENERSE ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))
            
            #ADELANTE4X POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Adelante4x()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE ADELANTE 3X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))
            
            #DETENERSE POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Detenerse()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DETERNERSE ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))
            
            #ATRAS4X POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Atras4x()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE ATRAS 4X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))
            
            #DETENERSE POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Detenerse()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE DETENERSE  ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))
            
            #ADELANTE3X POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Adelante3x()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE ADELANTE 3X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))
            
            #DETENSERSE POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Detenerse()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE DETENERSE ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))
            
            #ATRAS3X POR 3 SEGUNDOS
            start = time.time()
            while(time.time()-start< 3.0):
                LM.Atras3x()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE ATRAS 3X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))
            
            #DETENERSE POR 1 SEGUNDOS
            start = time.time()
            while(time.time()-start< 1.0):
                LM.Detenerse()
                #LECTURAS
                iAB = Frontal.ReadCurrents(address)
                iCD = Trasero.ReadCurrents(address)
                pwmAB = Frontal.ReadPWMs(address)
                pwmCD = Trasero.ReadPWMs(address)
                lectura = displayspeed()
                writer.writerow([(time.time()- start_time), lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], float(iAB[1])/100, float(iAB[2])/100, float(iCD[1])/100, float(iCD[2])/100, pwmAB[1], pwmAB[2], pwmCD[1], pwmCD[2]])
                time.sleep(0.01)
            print("\n--- FIN DE DETENERSE ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

            ### FIN DE LA PRUEBA
            print("\n --- FIN DE LA PRUEBA ---")	   
            start = time.time()
            LM.Detenerse()
            time.sleep(1)
            print("\n--- %s seconds ---\n" % (time.time() - start))
            rep = rep + 1

if __name__ == '__main__':
    main()
