import time
import board
from adafruit_bme280 import basic as adafruit_bme280

spi = board.SPI()
bme_cs = digitalio.DigitalInOut(board.D10)
bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, bme_cs)

bme280.sea_level_pressure = 1013.25

while True:
  print(bme280.Temperature)
  time.sleep(2)
