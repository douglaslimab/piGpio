from flask import Flask, render_template
import serial

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
	if relay == 'relay1':
		data = 'Relay 1 ' + state
	elif relay == 'relay2':
		data = 'Relay 2 ' + state
	elif relay == 'relay3':
		data = 'Relay 3 ' + state
	elif relay == 'relay4':
		data = 'Relay 4 ' + state
	elif relay == 'relay5':
		data = 'Relay 5 ' + state
	elif relay == 'relay6':
		data = 'Relay 6 ' + state
	elif relay == 'relay7':
		data = 'Relay 7 ' + state
	elif relay == 'relay8':
		data = 'Relay 8 ' + state
	elif relay == 'relay9':
		data = 'Relay 9 ' + state
	else:
		data = 'invalid entry'
	return data

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
	app.run(host="192.168.0.80", port=8000, debug=True)
