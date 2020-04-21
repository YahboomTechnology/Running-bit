from microbit import *
import superbit
import radio
import neopixel
Red = (255, 0, 0)
Orange = (255, 165, 0)
Yellow = (255, 255, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Violet = (148, 0, 211)
White = (255, 255, 255)
color_lib = {'Red': Red, 'Orange': Orange, 'Yellow': Yellow, 'Green': Green,
'Blue': Blue, 'Violet': Violet, 'White': White}
def RGBLight_more_show(first, num, color):
    global np

    np.clear()
    for i in range(first, first + num):
        np[i] = color_lib[color]
    np.show()
np = neopixel.NeoPixel(pin12, 4)
display.show(Image.HEART)
radio.on()
radio.config(group=1)
while True:
    incoming = radio.receive()
    if incoming == 'up':
        superbit.motor_control(superbit.M1, 255, 0)
        superbit.motor_control(superbit.M3, 255, 0)
    elif incoming == 'down':
        superbit.motor_control(superbit.M1, -255, 0)
        superbit.motor_control(superbit.M3, -255, 0)
    elif incoming == 'left':
        superbit.motor_control(superbit.M1, 0, 0)
        superbit.motor_control(superbit.M3, 255, 0)
    elif incoming == 'right':
        superbit.motor_control(superbit.M1, 255, 0)
        superbit.motor_control(superbit.M3, 0, 0)
    elif incoming == 'stop':
        superbit.motor_control(superbit.M1, 0, 0)
        superbit.motor_control(superbit.M3, 0, 0)
    elif incoming == 'R':
        RGBLight_more_show(0, 4, 'Red')
        superbit.servo270(superbit.S1, 60)
    elif incoming == 'G':
        RGBLight_more_show(0, 4, 'Green')
        superbit.servo270(superbit.S1, 120)
    elif incoming == 'B':
        RGBLight_more_show(0, 4, 'Blue')
    elif incoming == 'Y':
        RGBLight_more_show(0, 4, 'Yellow')
        superbit.servo270(superbit.S1, 180)


