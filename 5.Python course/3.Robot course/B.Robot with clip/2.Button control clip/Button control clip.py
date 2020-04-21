from microbit import *
import superbit

display.show(Image.HAPPY)
superbit.servo270(superbit.S1, -0)
while True:
    if button_a.is_pressed() is True and button_b.is_pressed() is False:
        superbit.servo270(superbit.S1, 0)
    elif button_a.is_pressed() is False and button_b.is_pressed() is True:
        superbit.servo270(superbit.S1, 60)