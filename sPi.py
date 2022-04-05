import spidev
import time

bus = 1
device = 1

spi = spidev.SpiDev()

spi.open(bus, device)

spi.max_speed_hz = 500000
spi.mode = 0

while True:
  msg = [0xFE]
  res = spi.readbytes(msg)
  print(res)
  time.sleep(1)
