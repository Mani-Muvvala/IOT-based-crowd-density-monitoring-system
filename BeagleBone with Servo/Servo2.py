#! /usr/bin/python3
import Adafruit_BBIO.PWM as PWM
import time
import sys

servo_pin = "P8_19"                                    # servo pin number
                                                       
 user_input = int(sys.argv[1])                         # stores first argument while calling program

if user_input == 1:                                    # executes if user input =1
        
#       print("opened")
                                                       # duty cycles=97 for opening ~0 degrees
        PWM.start(servo_pin, 92, 60, 1)
                                                      
        time.sleep(1)                                  # need time gap to execute previous cmd
        
        PWM.stop(servo_pin)                            # stops pwm at servo pin
       
        PWM.cleanup()                                  # cleans up inmported pwm functions from memory
        
else:
                                                       # runs when user input is 0 for close
        PWM.start(servo_pin, 97.4, 60, 1)
        
        time.sleep(1)                                  # time gap to execute code
       
        PWM.stop(servo_pin)                            # stops pwm
        
        PWM.cleanup()                                  # cleans memory
 
 #      print("closed")






