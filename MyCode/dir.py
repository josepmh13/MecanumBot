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