import serial

uart2 = serial.Serial(port='/dev/ttyAMA1', baudrate=9600)
uart4 = serial.Serial(port='/dev/ttyAMA2', baudrate=9600)

while True:
	print(uart2.read())
	print(uart4.read())
