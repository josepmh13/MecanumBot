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
    time.sleep(2)

    with open("csvMAX.csv", "wb") as f:
        writer = csv.writer(f,  delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
	writer.writerow(['Tiempo', 'EncA', 'EncB', 'EncC', 'EncD', 'vA', 'vB', 'vC', 'vD','iA','iB', 'iC', 'iD', 'pwmA', 'pwmB', 'pwmC', 'pwmD'])
        rep=0
	#try:		
        while(rep<1):     	
	    #while (Ein[0]<1 and Ein[1]<1 and Ein[2] <1 and Ein[3] <1):
            start = time.time()
            while(time.time()-start< 2.0):
		#LM.Adelante2x()
		LM.Atras2x() 	
                L1 = LM.EDV()
	 	L2 = LM.display_IP()
		#print((time.time()-start_time))
        	writer.writerow([(time.time()- start), L1[0], L1[1], L1[2], L1[3], L1[4], L1[5], L1[6], L1[7], L2[0], L2[1], L2[2], L2[3], L2[4], L2[5], L2[6], L2[7]])
		time.sleep(0.01)
                #Ein =[abs(L1[0]), abs(L1[1]), abs(L1[2]), abs(L1[3])]
	    
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
