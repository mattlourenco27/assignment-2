# Created by: Matthew Lourenco
# Created on: 26 Sept 2016
# This is a program that finds the distance an object is above the ground after a given number of seconds if it is dropped from a 100m cliff.

import ui

GRAVITY = 9.81

def calculate_touch_up_inside(sender):
    #calculates the gravity baised on the inputed time
    
    #input
    seconds = float(view['seconds_textfield'].text)
    
    #process
    height = 100 - ( GRAVITY * (seconds ** 2) ) / 2
    
    #output
    view['answer_label'].text = str( round(height,3) )

view = ui.load_view()
view.present('full_screen')
