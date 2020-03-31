from microbit import *
import superbit
import microbit
display.show(Image.HAPPY)
superbit.servo270(superbit.S1, 120)
while True:
    if button_a.is_pressed() is True and button_b.is_pressed() is False:
        superbit.servo270(superbit.S1, 120)
    elif button_a.is_pressed() is False and button_b.is_pressed() is True:
        superbit.servo270(superbit.S1, 60)
    elif button_a.is_pressed() is True and button_b.is_pressed() is True:
        microbit.sleep(50)
        if button_a.is_pressed() is True and button_b.is_pressed() is True:
            superbit.servo270(superbit.S1, 180)
