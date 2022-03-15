from flask import Flask, render_template
import serial

uart2 = serial.Serial(port='/dev/ttyAMA1', baudrate=9600)
uart4 = serial.Serial(port='/dev/ttyAMA2', baudrate=9600)

app = Flask(__name__)

@app.route("/")
def home():
	uart2.write('a')
	return render_template('index.html')

@app.route("/write2a")
def write2():
	uart2.write('hello from uart2')
	return "uart2 >> uart4"

@app.route("/read2")
def read2():
	data = uart2.read()
	return data

@app.route("/write4b")
def write4():
	uart4.write('hello from uart4')
	return "uart4 >> uart2"

@app.route("/read4")
def read4():
	return uart4.read()

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000, debug=True)
