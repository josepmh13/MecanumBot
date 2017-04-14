# coding=utf-8
import csv
import time

def main():

    start_time = time.time()

    with open("csvFile.csv", "wb") as f:
        writer = csv.writer(f,  delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        rep = 0
        while (rep<4):
                writer.writerow(['Tiempo', 'EncA', 'EncB', 'EncC', 'EncD', 'iA','iB', 'iC', 'iD'])
                rep = rep+1

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()

             