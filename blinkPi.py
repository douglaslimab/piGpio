import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

relay_1 = 13
relay_2 = 26
relay_3 = 14
relay_4 = 15
relay_5 = 23
relay_6 = 24
relay_7 = 25
relay_8 = 12
relay_9 = 16

add1_0 = 2
add1_1 = 17

add2_0 = 22
add2_1 = 10
add2_2 = 11

GPIO.setup(relay_1, GPIO.OUT)
GPIO.setup(relay_2, GPIO.OUT)
GPIO.setup(relay_3, GPIO.OUT)
GPIO.setup(relay_4, GPIO.OUT)
GPIO.setup(relay_5, GPIO.OUT)
GPIO.setup(relay_6, GPIO.OUT)
GPIO.setup(relay_7, GPIO.OUT)
GPIO.setup(relay_8, GPIO.OUT)
GPIO.setup(relay_9, GPIO.OUT)
GPIO.setup(add1_0, GPIO.OUT)
GPIO.setup(add1_1, GPIO.OUT)
GPIO.setup(add2_0, GPIO.OUT)
GPIO.setup(add2_1, GPIO.OUT)
GPIO.setup(add2_2, GPIO.OUT)

while(True):
	GPIO.output(relay_1, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(relay_1, GPIO.LOW)
	time.sleep(1)
	GPIO.output(relay_2, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(relay_2, GPIO.LOW)
	time.sleep(1)
	GPIO.output(relay_3, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(relay_3, GPIO.LOW)
	time.sleep(1)
	GPIO.output(relay_4, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(relay_4, GPIO.LOW)
	time.sleep(1)
	GPIO.output(relay_5, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(relay_5, GPIO.LOW)
	time.sleep(1)
	GPIO.output(relay_6, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(relay_6, GPIO.LOW)
	time.sleep(1)
	GPIO.output(relay_7, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(relay_7, GPIO.LOW)
	time.sleep(1)
	GPIO.output(relay_8, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(relay_8, GPIO.LOW)
	time.sleep(1)
	GPIO.output(relay_9, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(relay_9, GPIO.LOW)
	time.sleep(1)

	GPIO.output(add1_0, GPIO.HIGH)
	GPIO.output(add1_1, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(add1_0, GPIO.LOW)
	GPIO.output(add1_1, GPIO.LOW)
	time.sleep(1)

	GPIO.output(add2_0, GPIO.HIGH)
	GPIO.output(add2_1, GPIO.HIGH)
	GPIO.output(add2_2, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(add2_0, GPIO.LOW)
	GPIO.output(add2_1, GPIO.LOW)
	GPIO.output(add2_2, GPIO.LOW)
	time.sleep(1)
