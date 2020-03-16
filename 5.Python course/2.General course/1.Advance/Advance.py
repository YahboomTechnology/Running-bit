from microbit import *
import superbit

display.show(Image.HEART)

while True:
    superbit.motor_control(superbit.M1, 255, 0)
    superbit.motor_control(superbit.M3, 255, 0)