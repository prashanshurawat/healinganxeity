import serial
import time
import os
import sys
def UI():
    os.system('python UI1.py')
ser = serial.Serial('COM19',9600)
time.sleep(2)
for i in range(300):

    b=ser.readline()
    string_n = b.decode()
    string = string_n.strip()
    inches = float(string)
    if inches<=48:
        UI()
    
ser.close()

