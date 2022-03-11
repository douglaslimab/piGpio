import serial

uart2 = serial.Serial(port='/dev/ttyAMA1', baudrate=9600)
uart4 = serial.Serial(port='/dev/ttyAMA2', baudrate=9600)

def write_2(msg):
    uart2.write(bytes(msg, 'utf-8'))

def read_2():
    return uart2.readline()

def write_4(msg):
    uart4.write(bytes(msg, 'utf-8'))

def read_4():
    return  uart4.readline()

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('PyCharm')