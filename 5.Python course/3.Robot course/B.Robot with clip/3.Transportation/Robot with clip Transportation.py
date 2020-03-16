from microbit import *
import superbit
import microbit
display.show(Image.HAPPY)
superbit.servo270(superbit.S1, 120)
while True:
    if button_a.is_pressed():
        superbit.servo270(superbit.S1, 180)
        microbit.sleep(500)
        superbit.motor_control(superbit.M1, 255, 0)
        superbit.motor_control(superbit.M3, 255, 0)
        microbit.sleep(2000)
        superbit.motor_control(superbit.M1, 0, 0)
        superbit.motor_control(superbit.M3, 0, 0)
        superbit.servo270(superbit.S1, 60)
        microbit.sleep(500)
        superbit.servo270(superbit.S1, 120)
        microbit.sleep(500)
        superbit.motor_control(superbit.M1, -255, 0)
        superbit.motor_control(superbit.M3, -255, 0)
        microbit.sleep(2000)
        superbit.motor_control(superbit.M1, 0, 0)
        superbit.motor_control(superbit.M3, 0, 0)
