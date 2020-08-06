from machine import Pin,PWM
import _thread
import utime

led_blue = PWM(Pin(0), freq=5000, duty=1023) 
led_green = PWM(Pin(2), freq=5000, duty=1023) 
led_red = PWM(Pin(4), freq=5000, duty=1023) 

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
orange = (255,100,0)
black = (0,0,0)

do_blinking = False
blink_execute = False

def color(color:tuple):
    _stop_task_()
    return _set_color_(color)

def blink(color:tuple, duration, second_color:tuple = black):
    _stop_task_()
    _thread.start_new_thread(_blink_loop_,(color,duration,second_color))    
    return color


def _set_color_(color):
    led_red.duty(1023-color[0]*4)
    led_green.duty(1023-color[1]*4)
    led_blue.duty(1023-color[2]*4)
    return color

def _stop_task_():
    global do_blinking, blink_execute
    if do_blinking == True:
        do_blinking = False
        while blink_execute:
            pass

def _wait_(duration):
    global do_blinking
    while(duration >0):
        utime.sleep_us(750) # adapted by feeling. longer due to other cmds
        duration = duration -1
        if (do_blinking == False):
            return  

def _blink_loop_(color, duration, second_color):
    global do_blinking, blink_execute
    do_blinking = True
    blink_execute = True
    while(do_blinking):
        _set_color_(color)
        _wait_(duration)
        _set_color_(second_color)
        _wait_(duration)
    blink_execute = False

def __init__():
    print ("test")