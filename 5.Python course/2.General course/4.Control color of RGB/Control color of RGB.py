from microbit import *
import neopixel
import microbit

Red = (255, 0, 0)
Orange = (255, 165, 0)
Yellow = (255, 255, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Violet = (148, 0, 211)
White = (255, 255, 255)
color_lib = {
    'Red': Red, 'Orange': Orange, 'Yellow': Yellow, 'Green': Green,
    'Blue': Blue, 'Violet': Violet, 'White': White}

def RGBLight_more_show(first, num, color):
    global np
    np.clear()
    for i in range(first, first + num):
        np[i] = color_lib[color]
    np.show()


display.show(Image.HAPPY)
np = neopixel.NeoPixel(pin12, 4)
while True:
    RGBLight_more_show(0, 4, 'Red')
    microbit.sleep(1000)
    RGBLight_more_show(0, 4, 'Green')
    microbit.sleep(1000)
    RGBLight_more_show(0, 4, 'Blue')
    microbit.sleep(1000)