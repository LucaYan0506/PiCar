import keyboard
import time
from SunFounder_Ultrasonic_Avoidance import Ultrasonic_Avoidance
from picar import front_wheels
from picar import back_wheels
import time
import picar
import random

force_turning = 0    # 0 = random direction, 1 = force left, 2 = force right, 3 = orderdly

picar.setup()

ua = Ultrasonic_Avoidance.Ultrasonic_Avoidance(20)
fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')
fw.turning_max = 45

forward_speed = 40
backward_speed = 40

back_distance = 10
turn_distance = 20

while True:
    left_right = -1
    forward_backgward = -1

    if keyboard.is_pressed('w') or keyboard.is_pressed('up'): 
        forward_backgward = 1
    elif keyboard.is_pressed('s') or keyboard.is_pressed('down'): 
        forward_backgward = 0

    if keyboard.is_pressed('a') or keyboard.is_pressed('left'): 
        left_right  = 1
    elif keyboard.is_pressed('d') or keyboard.is_pressed('right'): 
        left_right = 0

  
    if (forward_backgward == -1):
        print("The car is stopped")
    else:
        temp = "The car is going "
        if (forward_backgward == 1):
            temp += "forward"
        else:
            temp += "backward"

        if left_right == 1:
            temp += " and turning right"
            fw.turn(90)
        elif left_right == 0:
            temp += " and turing left"
            fw.turn(-90)
        else:
            fw.turn_straight()

        if (forward_backgward == 1):
            bw.forward()
        else:
            bw.backward()

        print('The car is going ' + temp)
    time.sleep(1)