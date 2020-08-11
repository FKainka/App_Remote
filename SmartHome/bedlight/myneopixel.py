
import machine
import neopixel
from bedlight.colorsys import *
import math
import time

green = (255,0,0)
red = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
orange = (255,100,0)
black = (0,0,0)

def rainbow():
    global np
    nr = np.n
    dif = 240/nr
    grad = 0
    for i in range(nr):
        rgb = hsv2rgb(grad,1,1)
        myorder = [1,0,2]
        np[i] = [rgb[i] for i in myorder]  #reorder
        grad = grad + dif
    np.write()

def half(color1,color2):
    global np
    nr = np.n
    for i in range(nr):
        if i<=nr/2 and color1 is not None:
            np[i] = color1
        elif i>nr/2 and color2 is not None:
            np[i] = color2
    np.write()

def brightness(bright):
    global np
    #0-100
    for i in range(np.n):
        r,g,b = np[i]
        if np[i] == (0,0,0):
            #print ("contine")
            continue
        h,s,v= rgb2hsv(r,g,b)
        v = bright /100
        np[i] = hsv2rgb(h,s,v)
        #print(np[i])
        np.write()

do_task = False
task_execute = False

def stop_task():
    _stop_task_()

def _stop_task_():
    global do_task, task_execute
    if do_task == True:
        do_task = False
        while task_execute:
            pass

def _wait_(duration):
    global do_task
    while(duration >0):
        time.sleep_us(500) # adapted by feeling. longer due to other cmds
        duration = duration -1
        if (do_task == False):
            return  

def _task_loop_(task, duration):
    global do_task, task_execute
    do_task = True
    task_execute = True
    #print(time.localtime())
    while(do_task):
        task()
        _wait_(duration)
    task_execute = False

def task_sundown():
    global task_progress
    if task_progress > 0:
        task_progress = task_progress -1
        brightness(task_progress)
    else :
        #print(time.localtime())
        _stop_task_()

def sundown(duration, color = None):
    #duration in seconds
    if color is not None:
        for i in range(np.n):
            np[i] = color
    _stop_task_() 
    global task_progress
    task_progress = 100
    wait_time = duration*1000 /100
    import _thread
    _thread.start_new_thread(_task_loop_,(task_sundown,wait_time))

def set_list(color_list):
    for i in range(np.n):
        np[i] = color_list[i]
    np.write()

def set_color(color):
    for i in range(np.n):
        np[i] = color
    np.write()


np = neopixel.NeoPixel(machine.Pin(13), 44)
rainbow()
#half(np,(255,0,0),(0,0,255))
#time.sleep(5)
#half(np,None,(0,255,255))
#time.sleep(5)
#half(np,(0,255,0),None)
#time.sleep(1)
#brightness(np,1)
#sundown(60*1)
