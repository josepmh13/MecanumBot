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

def main():

    Frontal.ResetEncoders(address)
    Trasero.ResetEncoders(address)
    time.sleep(1)

    with open("Ts6.csv", "wb") as f:
        writer = csv.writer(f,  delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(['Tiempo', 'EncA', 'EncB', 'EncC', 'EncD','vA', 'vB', 'vC', 'vD', 'iA','iB', 'iC', 'iD', 'pwmA', 'pwmB', 'pwmC', 'pwmD'])

        rep=0
        while(rep<1):
        ##### ADELANTE1X POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Adelante1x()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE ADELANTE 1X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

	    ##### ADELANTE2X POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Adelante2x()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE ADELANTE 2X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

	    ##### ADELANTE3X POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Adelante3x()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE ADELANTE 3X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

        ##### ADELANTE4X POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Adelante4x()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE ADELANTE 4X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

        ##### ADELANTE5X POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Adelante5x()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE ADELANTE 5X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

        ##### ADELANTE4X POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Adelante4x()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE ADELANTE 4X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

        ##### ADELANTE3X POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Adelante3x()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE ADELANTE 3X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

        ##### ADELANTE2X POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Adelante2x()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE ADELANTE 2X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

        ##### ADELANTE1X POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Adelante1x()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE ADELANTE 1X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

        ##### DETENERSE POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Detenerse()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE DETENERSE ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

        ##### ATRAS1X POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Atras1x()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE ATRAS 1X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

        ##### ATRAS2X POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Atras2x()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE ATRAS 2X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

        ##### ATRAS3X POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Atras3x()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE ATRAS 3X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

        ##### ATRAS4X POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Atras4x()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE ATRAS 4X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

        ##### ATRAS5X POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Atras5x()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE ATRAS 5X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

        ##### ATRAS4X POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Atras4x()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE ATRAS 4X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

        ##### ATRAS3X POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Atras3x()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE ATRAS 3X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

        ##### ATRAS2X POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Atras2x()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE ATRAS 2X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

        ##### ATRAS1X POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Atras1x()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE ATRAS 1X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

        ##### DETENERSE POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Detenerse()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE DETENERSE ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

	    ##### ADELANTE2X POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Adelante2x()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE ADELANTE2X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

        ##### ATRAS2X POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Atras2x()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE ATRAS 2X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

        ##### DETENERSE POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Detenerse()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE DETENERSE ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

        ##### ADELANTE4X POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Adelante4x()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE ADELANTE4X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

        ##### DETENERSE POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Detenerse()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE DETENERSE ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

        ##### ATRAS4X POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Atras4x()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE ATRAS 4X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

        ##### DETENERSE POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Detenerse()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE DETENERSE ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

        ##### ADELANTE3X POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Adelante3x()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE ADELANTE3X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

        ##### DETENERSE POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Detenerse()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE DETENSERSE ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

        ##### ATRAS3X POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Atras3x()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE ATRAS 3X ----")
            print("\n--- %s seconds ---\n" % (time.time() - start))

        ##### DETENERSE POR 3 SEGUNDOS #####
            start = time.time()
            last = start
            while(time.time()-start< 3.0):
                inicio = time.time()
                if (inicio-last)>=0.05:
                    savelast = last
                    last = inicio
                    LM.Detenerse()
                    LM.writeCSV(writer,start,savelast)
            print("\n--- FIN DE DETENSERSE ----")
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


