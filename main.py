#set up onboard ws2812 on GP11

import neopixel
from machine import Pin

light_pin = Pin(11, mode=Pin.OUT)
light = neopixel.NeoPixel(light_pin, 2)

light.fill((15, 15, 15))
light.write()
