import RPi.GPIO as GPIO
 import time
 GPIO.setmode(GPIO.BOARD)
 GPIO.setwarnings(False)button=12
 DC_motor_a=7 
DC_motor_b=11 
GPIO.setup(DC_motor_a,GPIO.OUT) GPIO.setup(DC_motor_b,GPIO.OUT) GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_UP) 
while(1): 
    if GPIO.input(button)==GPIO.LOW: 
        GPIO.output(DC_motor_a,GPIO.HIGH)
        GPIO.output(DC_motor_b,GPIO.LOW)time.sleep(0.1) 
    else: GPIO.output(DC_motor_a,GPIO.LOW)
    GPIO.output(DC_motor_b,GPIO.HIGH)
    time.sleep(0.1) 
