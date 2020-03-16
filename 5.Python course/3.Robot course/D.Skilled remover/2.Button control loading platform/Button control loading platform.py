from microbit import *
import superbit

display.show(Image.HAPPY)
superbit.servo270(superbit.S1, 240)

while True:
    if button_a.is_pressed():
        superbit.servo270(superbit.S1, 240)
    elif button_b.is_pressed():
        superbit.servo270(superbit.S1, 60)
