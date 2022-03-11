import serial
import time

uart2 = serial.Serial(port='/dev/ttyAMA1', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
uart4 = serial.Serial(port='/dev/ttyAMA2', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

while True:
    #uart2 writing on uart4
    uart2.write('abc')

    #reading on uart2 from uart4
    uart4.write('123')

    #uart4 writing on uart2
    output = uart4.read()
    print(output)

    #reading on uart4 from uart2
    output = uart2.read()
    print(output)

    time.sleep(1)