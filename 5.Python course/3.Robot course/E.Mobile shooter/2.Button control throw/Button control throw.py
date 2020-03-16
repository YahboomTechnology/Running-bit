from microbit import *
import superbit

display.show(Image.HAPPY)
superbit.servo270(superbit.S1, 105)

while True:
    if button_a.is_pressed():
        superbit.servo270(superbit.S1, 135)
    elif button_b.is_pressed():
        superbit.servo270(superbit.S1, 105)
