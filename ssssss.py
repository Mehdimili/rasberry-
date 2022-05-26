Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#!/usr/bin/python
import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 976000

def write_pot(input):
    msb = input >> 8
    lsb = input & 0xFF
    spi.xfer([msb, lsb])

while True:
    for i in range(0x00, 0x1FF, 1):
        write_pot(i)
        time.sleep(.005)
    for i in range(0x1FF, 0x00, -1):
        write_pot(i)
        time.sleep(.005)