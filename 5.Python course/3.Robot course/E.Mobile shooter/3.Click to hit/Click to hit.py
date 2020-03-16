from microbit import *
import superbit
import microbit

display.show(Image.HAPPY)
superbit.servo270(superbit.S1, 105)

while True:
    if button_a.is_pressed():
        superbit.motor_control_dual(superbit.M1, superbit.M3, 255, 255, 0)
        microbit.sleep(1000)
        superbit.motor_control_dual(superbit.M1, superbit.M3, 0, 0, 0)
        superbit.servo270(superbit.S1, 135)
        microbit.sleep(500)
        superbit.servo270(superbit.S1, 105)
        microbit.sleep(500)
        superbit.motor_control_dual(superbit.M1, superbit.M3, -255, -255, 0)
        microbit.sleep(1000)
        superbit.motor_control_dual(superbit.M1, superbit.M3, 0, 0, 0)

