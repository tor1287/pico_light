import neopixel
import time
from machine import Pin

light_pin = Pin(11, mode=Pin.OUT)
light = neopixel.NeoPixel(light_pin, 2)
button = Pin(20, mode=Pin.IN, pull=Pin.PULL_UP)

def light_red():
    light.fill((15, 0, 0))
    light.write()

def light_green():
    light.fill((0, 15, 0))
    light.write()

def light_blue():
    light.fill((0, 0, 15))
    light.write()


def button_handler(button):
    light.fill((15, 15, 15))
    light.write()
    time.sleep(1)

button.irq(button_handler, trigger=button.IRQ_FALLING)
