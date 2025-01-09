#!/usr/bin/env python3
import serial

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()

    while True:
        cc=str(ser.readline())
        print("cc:",cc)
        
        """if ser.in_waiting > 0:
            cc=str(ser.readline())
            print("cc:",cc)
            line = ser.readline().decode('utf-8').rstrip()
            #print(line)
            """