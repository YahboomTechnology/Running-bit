from microbit import *
import superbit
import microbit
display.show(Image.HAPPY)

while True:
    superbit.motor_control(superbit.M1, 0, 0)
    superbit.motor_control(superbit.M3, 0, 0)
    microbit.sleep(1000)
    superbit.motor_control(superbit.M1, 125, 0)
    superbit.motor_control(superbit.M3, 125, 0)
    microbit.sleep(1000)
    superbit.motor_control(superbit.M1, 255, 0)
    superbit.motor_control(superbit.M3, 255, 0)
    microbit.sleep(1000)
    superbit.motor_control(superbit.M1, 125, 0)
    superbit.motor_control(superbit.M3, 125, 0)
    microbit.sleep(1000)