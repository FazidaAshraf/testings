import serial

arduino_port = '/dev/ttyUSB0'  # Update as needed
baud_rate = 9600

try:
    ser = serial.Serial(arduino_port, baud_rate, timeout=1)
    print("Connected to Arduino")

    while True:
        if ser.in_waiting > 0:
            print("im in the loop!!!")
            data = ser.readline().decode('utf-8').strip()
            print(f"Received: {data}")

except Exception as e:
    print(f"Error: {e}")

finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
