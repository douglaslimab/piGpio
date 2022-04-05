from flask import Flask, render_template
import serial
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

relays = {
	'relay1': 13,
	'relay2': 26,
	'relay3': 14,
	'relay4': 15,
	'relay5': 23,
	'relay6': 24,
	'relay7': 25,
	'relay8': 12,
	'relay9': 16
	}

uart2_address = 0x00
uart4_address = 0x00

GPIO.setup(2, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

GPIO.setup(20, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

for relay in relays.values():
    GPIO.setup(relay, GPIO.OUT)

uart2 = serial.Serial(port='/dev/ttyAMA1', baudrate=9600)
uart4 = serial.Serial(port='/dev/ttyAMA2', baudrate=9600)

app = Flask(__name__)

def inc_uart2_address():
	global uart2_address
	uart2_address += 1
	GPIO.output(2, (uart2_address & 1))
	GPIO.output(17, (uart2_address & 2))

def inc_uart4_address():
	global uart4_address
	uart4_address += 1
	GPIO.output(20, (uart4_address & 1))
	GPIO.output(10, (uart4_address & 2))
	GPIO.output(11, (uart4_address & 4))

@app.route("/gpio/getState")
def getRelayState():
	relays_state = {
		'relay1': GPIO.digitalRead(13),
		'relay2': GPIO.digitalRead(26),
		'relay3': GPIO.digitalRead(14),
		'relay4': GPIO.digitalRead(15),
		'relay5': GPIO.digitalRead(23),
		'relay6': GPIO.digitalRead(24),
		'relay7': GPIO.digitalRead(25),
		'relay8': GPIO.digitalRead(12),
		'relay9': GPIO.digitalRead(16)
		}
	return relays_state

@app.route("/")
def home():
	uart2.write('home')
	uart4.write('home')
	return render_template('index.html')

@app.route("/address/<uart>")
def set_address(uart):
	if(uart == "2"):
		inc_uart2_address()
	elif(uart == "4"):
		inc_uart4_address()
	return "ok"

@app.route("/write/<uart>/<res>")
def write(uart, res):
	if uart == 'uart2':
		uart2.write(bytes(res))
	elif uart == 'uart4':
		uart4.write(bytes(res))
	else:
		data = 'uart error'
	return res + ' sent from ' + uart

@app.route("/read/<uart>")
def read(uart):
	if uart == 'uart2':
		data = uart2.read(5)
	elif uart == 'uart4':
		data = uart4.read(5)
	else:
		data = 'uart error'
	return data + ' read on the ' + uart

@app.route("/gpio/<relay>/<state>")
def toggle(relay, state):
	if state == 'on':
		GPIO.output(relays[relay], GPIO.HIGH)
	elif state == 'off':
		GPIO.output(relays[relay], GPIO.LOW)
	elif state == 'all':
		for relay in relays:
			GPIO.output(relays[relay], GPIO.HIGH)
	elif state == 'none':
		for relay in relays:
			GPIO.output(relays[relay], GPIO.LOW)
	return render_template('index.html')

@app.route("/uart/<address>/<data>")
def send(address, data):
	return render_template('index.html')

@app.route("/current")
def current():
	return 'get current'

@app.route("/temperature")
def temperature():
	return 'get temperature'

@app.route("/humidity")
def humidity():
	return 'get humidity'

@app.route("/pressure")
def pressure():
	return 'get pressure'

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000, debug=True)


#	/relay/1/on
#	/uart_test/2/read
#	/sensors/temperature
