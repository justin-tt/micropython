from microbit import *
pin1.set_analog_period(20)

state = 0
while True:

    pin1.write_analog(state)
    sleep(100)
    
    if button_a.is_pressed():
        state = 1
    if button_b.is_pressed():
        state = 180
    if button_a.is_pressed() and button_b.is_pressed():
        state = 0