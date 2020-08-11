from bedlight.myneopixel import *
from machine import TouchPad, Pin
import time
import tools.rgb

threshold = 250
on = False

## To deactivate Light
from machine import Pin,PWM
led_blue = PWM(Pin(0), freq=5000, duty=1023) 
led_green = PWM(Pin(2), freq=5000, duty=1023) 
led_red = PWM(Pin(4), freq=5000, duty=1023) 


t1 = TouchPad(Pin(32))   #33
t2 = TouchPad(Pin(33))   #33

def do_sundown():
    sundown(60*30)

def do_papa():
    half(yellow,black)
    brightness(50)

def do_both():
    half(green,red)

def do_night():
    half(red,black)
    brightness(10)

list_bedfunctions=[rainbow,do_both,do_papa,do_sundown,do_night]
list_index = 0

while(True):
    if (t1.read()< threshold):
        if not on:
            stop_task()
            list_bedfunctions[list_index]()
            on = True
        else:
            stop_task()
            set_color(black)
            on = False

        while t1.read() < threshold:
            time.sleep_ms(500)

    if (t2.read()< threshold):
        if not on:
            pass
        else:
            stop_task()
            list_index = list_index +1
            if list_index > len(list_bedfunctions)-1:
                list_index = 0
            list_bedfunctions[list_index]()

        while t2.read() < threshold:
            time.sleep_ms(500)



