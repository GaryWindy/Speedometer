from machine import Pin
import utime
import time

#sensor is hall sensor omnipolar switch wire to pin 5
sensor = Pin(5,Pin.IN)
#pins selecting ones -10, tens -11, hundreds -12
digit_pins = [
    Pin(10,Pin.OUT),
    Pin(11,Pin.OUT),
    Pin(12,Pin.OUT),
    ]
#Pins output BCD to 74LS47 
segment_pins = [
    Pin(18,Pin.OUT),
    Pin(19,Pin.OUT),
    Pin(20,Pin.OUT),
    Pin(21,Pin.OUT)
    ]
#binary input to 74LS47, reversed for shift input
numbers_list = [
    [0, 0, 0, 0],#0
    [1, 0, 0, 0],#1
    [0, 1, 0, 0],#2
    [1, 1, 0, 0],#3
    [0, 0, 1, 0],#4
    [1, 0, 1, 0],#5
    [0, 1, 1, 0],#6
    [1, 1, 1, 0],#7
    [0, 0, 0, 1],#8
    [1, 0, 0, 1],#9
    ]
#clears display
def clear():
    for i in segment_pins:
        i.value(1)
clear()
#this is where a digit from numbers_list is assigned to segment_pins using speed
def set_sequence(speed): #apply numbers list to pins in sequence to generate a digit output using set_sequence(x)
    for x in range (0,4):
        segment_pins[x].value(numbers_list[speed][x])
#this is where speed will be defined
global ticks = 0
speed_list = [4, ticks, 0]
#this defines a function which blinks the digits one at a time
def mplex():
    mp_timer = 0
    while mp_timer <300:
        for i in range(len(digit_pins)):
            set_sequence(speed_list[i])
            digit_pins[i].value(0)
            utime.sleep(0.001)
            digit_pins[i].value(1)
            utime.sleep(0.001)
            mp_timer += 1
#BOTH EDGE DETECTION FUNCTION - x is run when pin state changes
#start 'ticks' at 0
#gets back the new counter value#Loops the function until the counter reaches 10
#while ticks < 10:
#    ticks +=1
#    mplex()
#    print(ticks)
#
#
#Some other dudes RPM Counter--------------------------------------
#last_time = time.time()
#this_time = time.time()
#def events_per_time(channel):   
#    global ticks, this_time, last_time
#   this_time=time.time()
#   ticks=1/(this_time - last_time)
#   print('RPM = ',ticks)
#   last_time = this_time
#   return()
#sensor.irq(trigger=Pin.IRQ_RISING, handler=events_per_time)
#-------------------------------------------------------------------
#RISING EDGE DETECTION FUNCTION
#def callback(sensor):
#   print('pin change', sensor)
#sensor.irq(trigger=Pin.IRQ_RISING, handler=callback)
#------------------------------------------------------------------
#FALLING EDGE DETECTION FUNCTION
#def callback(sensor):
#   print('pin change', sensor)
#sensor.irq(trigger=Pin.IRQ_FALLING, handler=callback)
#-----------------------------------------------------------------
#TEST INPUT CIRCUIT:
#while True:
#print(sensor.value())
#  utime.sleep(1)