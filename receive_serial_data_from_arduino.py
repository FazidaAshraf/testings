#!/usr/bin/env python3
import serial

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()

    array_tmp = []

    while True:
        byte_read = ser.read() # Read bytes from serial port
        print("byte_read:", byte_read)
        if byte_read:#if not empty
            byte_char = byte_read.decode() # Decode bytes to string
            print("byte_char:", byte_char)
            array_tmp.append(byte_char)
            if byte_char == '\n':
                print(''.join(array_tmp)) # Print the received line
                print("array_tmp:", array_tmp) # Print the received line
                array_tmp = []

    ser.close() 