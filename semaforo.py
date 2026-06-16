from machine import Pin
import time

def gpio_set(pin,value):
  if value >= 1:
    Pin(pin, Pin.OUT).on()
  else:
    Pin(pin, Pin.OUT).off()


gpio_set((23), False)
gpio_set((22), False)
gpio_set((19), False)
while True:
  gpio_set((23), True)
  gpio_set((22), False)
  time.sleep(5)
  gpio_set((23), False)
  gpio_set((19), True)
  time.sleep(5)
  gpio_set((19), False)
  gpio_set((22), True)
  time.sleep(5)
