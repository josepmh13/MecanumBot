# coding=utf-8
import libmov as LM
from roboclaw import Roboclaw

#Linux comport name
Frontal = Roboclaw("/dev/ttyACM0",115200) #Para los motores frontales
Trasero = Roboclaw("/dev/ttyACM1",115200) #Para los motores traseros
Frontal.Open()
Trasero.Open()
address = 0x80


def main():
    LM.Detenerse()

if __name__ == '__main__':
    main()
