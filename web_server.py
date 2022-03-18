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

for relay in relays.values():
    GPIO.setup(relay, GPIO.OUT)

#GPIO.setup(relay1, GPIO.OUT)
#GPIO.setup(relay2, GPIO.OUT)
#GPIO.setup(relay3, GPIO.OUT)
#GPIO.setup(relay4, GPIO.OUT)
#GPIO.setup(relay5, GPIO.OUT)
#GPIO.setup(relay6, GPIO.OUT)
#GPIO.setup(relay7, GPIO.OUT)
#GPIO.setup(relay8, GPIO.OUT)
#GPIO.setup(relay9, GPIO.OUT)

uart2 = serial.Serial(port='/dev/ttyAMA1', baudrate=9600)
uart4 = serial.Serial(port='/dev/ttyAMA2', baudrate=9600)

app = Flask(__name__)

@app.route("/")
def home():
	uart2.write('home')
	uart4.write('home')
	return render_template('index.html')

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
		data = uart2.read()
	elif uart == 'uart4':
		data = uart4.read()
	else:
		data = 'uart error'
	return data + ' read on the ' + uart

@app.route("/gpio/<relay>/<state>")
def toggle(relay, state):
	if state == 'on':
		GPIO.output(relays[relay], GPIO.HIGH)
	elif state == 'off':
		GPIO.output(relays[relay], GPIO.LOW)
	return render_template('index.html')

@app.route("/temperature")
def temperature():
	return 'get temperature'

@app.route("/humidity")
def humidity():
	return 'get humidity'

@app.route("/pressure")
def pressure():
	return 'get pressure'

@app.route("/write/<uart>/<res>")
def write(uart, res):
	if uart == "uart2":
		data = uart2.write(res)
	elif uart == "uart4":
		data = uart4.write(res)
	else:
		data = 'uart error'
	return data

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000, debug=True)


#	/relay/1/on
#	/uart_test/2/read
#	/sensors/temperature