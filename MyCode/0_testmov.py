# coding=utf-8
import time 
import subprocess
import libmov as LM
from roboclaw import Roboclaw

Frontal = Roboclaw("/dev/ttyACM0",115200) #Para los motores frontales
Trasero = Roboclaw("/dev/ttyACM1",115200) #Para los motores traseros
Frontal.Open()
Trasero.Open()
address = 0x80

### FORWARD 
def FORWARD():
    print("\nFORWARD ⇧\n")
    rep=0
    while(rep<1):
        LM.Adelante1x()
        time.sleep(2)
        LM.Detenerse()
        time.sleep(0.5)
        rep = rep + 1

### REVERSE
def REVERSE():
    print("\nREVERSE ⇩\n")
    rep=0
    while(rep<1):
        LM.Atras2x()
        time.sleep(2)
        LM.Detenerse()
        time.sleep(0.5)
        rep = rep + 1


### RIGHT SHIFT
def RIGHT():
    print("\nRIGHT ⇨\n")
    rep=0
    while(rep<1):
        LM.RIGHT2x()
        time.sleep(2)
        LM.Detenerse()
        time.sleep(0.5)
        rep = rep + 1

### LEFT SHIFT
def LEFT():
    print("\nLEFT ⇦\n")
    rep=0
    while(rep<1):
        LM.LEFT2x()
        time.sleep(2)
        LM.Detenerse()
        time.sleep(0.5)
        rep = rep + 1

### CW TURN
def CW():
    print("\nCW ↻\n")
    rep=0
    while(rep<1):
        LM.CW2x()
        time.sleep(2)
        LM.Detenerse()
        time.sleep(0.5)
        rep = rep + 1

### CCW TURN
def CCW():
    print("\nCCW ↺\n")
    rep=0
    while(rep<1):
        LM.CCW2x()
	time.sleep(2)
	LM.Detenerse()
	time.sleep(0.5)
	rep = rep + 1

### N0 TURN
def NO():
    print("\nNO ⇖\n")
    rep=0
    while(rep<1):
        LM.NO2x()
        time.sleep(2)
        LM.Detenerse()
        time.sleep(0.5)
        rep = rep + 1

### SE TURN
def SE():
    print("\nSE ⇘\n")
    rep=0
    while(rep<1):
        LM.SE2x()
        time.sleep(2)
        LM.Detenerse()
        time.sleep(0.5)
        rep = rep + 1

### NE TURN
def NE():
    print("\nNE ⇗\n")
    rep=0
    while(rep<1):
        LM.NE2x()
        time.sleep(2)
        LM.Detenerse()
        time.sleep(0.5)
        rep = rep + 1

### SO TURN
def SO():
    print("\nSO ⇙\n")
    rep=0
    while(rep<1):
        LM.SO2x()
        time.sleep(2)
        LM.Detenerse()
        time.sleep(0.5)
        rep = rep + 1

def main():
    
    while(1):
        subprocess.call(['tput', 'clear'])
        print("*******************************\n*** MOVIMIENTOS DEL MECANUM ***\n*******************************\n")
        print(" 0: Forward ⇧ \n 1: Reverse ⇩\n 2: Right ⇨\n 3: Left ⇦\n 4: CW ↻\n 5: CCW ↺\n 6: NO ⇖\n 7: SO ⇙\n 8: SE ⇘\n 9: NE ⇗\n")
        a = input("Ingrese el número del movimiento deseado: ")
        if a >=0 and a <=9:
            options = {0: FORWARD, 1: REVERSE, 2: RIGHT, 3: LEFT, 4: CW, 5: CCW, 6: NO, 7: SO, 8: SE, 9: NE}
            options[a]()
            time.sleep(2)
        else:
            print("\nEl número ingresado no es válido")
            time.sleep(2) 

if __name__ == '__main__':
    main()
