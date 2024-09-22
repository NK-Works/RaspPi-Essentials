# This code is written by Anneshu Nag, Student ID- 2210994760 #
#                       Dated- 12/09/2023                     #
#   Controlling LEDs connected to Raspberry Pi through GUI    #

import tkinter as tk
import RPi.GPIO as GPIO

# GPIO Pin numbers for the LEDs
LED_RED = 14
LED_YELLOW = 15 
LED_GREEN = 18 

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_YELLOW, GPIO.OUT) 
GPIO.setup(LED_GREEN, GPIO.OUT)  

# Variable to track the LED state
led_state = {
    LED_RED: False,
    LED_YELLOW: False,
    LED_GREEN: False, 
}

# Function to toggle LEDs
def toggle_led(led_pin):
    if led_state[led_pin]:
        # If the LED is already on, turn it off
        led_state[led_pin] = False
        GPIO.output(led_pin, GPIO.LOW)
    else:
        # If the LED is off, turn it on
        # Turn off all LEDs except the selected one
        switch_off_all_leds(except_led=led_pin)
        led_state[led_pin] = True
        GPIO.output(led_pin, GPIO.HIGH)
    
    # Update the radio button state
    update_radio_button_state(led_pin)

# Function to update the radio button state
def update_radio_button_state(led_pin):
    if led_pin == LED_RED:
        radio_red.select() if led_state[LED_RED] else radio_red.deselect()
    elif led_pin == LED_YELLOW:
        radio_yellow.select() if led_state[LED_YELLOW] else radio_yellow.deselect()  
    elif led_pin == LED_GREEN:
        radio_green.select() if led_state[LED_GREEN] else radio_green.deselect()  

# Function to switch on all LEDs
def switch_on_all_leds():
    for led_pin in led_state:
        led_state[led_pin] = True
        GPIO.output(led_pin, GPIO.HIGH)
    update_radio_button_state(LED_RED)  # Update the radio button states

# Function to switch off all LEDs
def switch_off_all_leds(except_led=None):
    for led_pin in led_state:
        if led_pin != except_led:
            led_state[led_pin] = False
            GPIO.output(led_pin, GPIO.LOW)
    update_radio_button_state(LED_RED)  # Update the radio button states

# Create the main window
window = tk.Tk()
window.title("LED Control")

# Set the window size to 600x400
window.geometry("600x400")

# Create a custom font with a larger size
custom_font = ("Helvetica", 16)

# Create a frame with a black background
frame_bg_color = "black"
button_frame = tk.Frame(window, bg=frame_bg_color)
button_frame.pack(fill="both", expand=True)

# Create a label for the title
title_label = tk.Label(button_frame, text="NK Works - LED CONTROL", font=("Helvetica", 24), fg="white", bg=frame_bg_color)
title_label.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

# Create introductory messages
intro_label = tk.Label(button_frame, text="Select an LED to turn on/off:", font=("Helvetica", 20), fg="white", bg=frame_bg_color)
intro_label.grid(row=1, column=0, columnspan=3, padx=20, pady=20)

# Create radio buttons with the corresponding background color, margins, larger size, and consistent activebackground
radio_red = tk.Radiobutton(button_frame, text="Red LED", value=LED_RED, variable=led_state[LED_RED], command=lambda: toggle_led(LED_RED), font=custom_font, background="red", activebackground="red", padx=10, pady=10, width=20, height=2)
radio_yellow = tk.Radiobutton(button_frame, text="Yellow LED", value=LED_YELLOW, variable=led_state[LED_YELLOW], command=lambda: toggle_led(LED_YELLOW), font=custom_font, background="yellow", activebackground="yellow", padx=10, pady=10, width=20, height=2)  
radio_green = tk.Radiobutton(button_frame, text="Green LED", value=LED_GREEN, variable=led_state[LED_GREEN], command=lambda: toggle_led(LED_GREEN), font=custom_font, background="green", activebackground="green", padx=10, pady=10, width=20, height=2)

# Create buttons to switch on all LEDs and switch off all LEDs
all_on_button = tk.Button(button_frame, text="On All", command=switch_on_all_leds, font=custom_font, padx=10, pady=10)
exit_button = tk.Button(button_frame, text="Exit", command=window.quit, font=custom_font, padx=10, pady=10)
all_off_button = tk.Button(button_frame, text="Off All", command=switch_off_all_leds, font=custom_font, padx=10, pady=10)

# Place widgets in the grid with center alignment
intro_label.grid(row=2, column=0, columnspan=3, padx=20, pady=20)
radio_red.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")
radio_yellow.grid(row=3, column=1, padx=20, pady=20, sticky="nsew")
radio_green.grid(row=3, column=2, padx=20, pady=20, sticky="nsew") 

all_on_button.grid(row=4, column=0, padx=20, pady=20, sticky="nsew")
exit_button.grid(row=4, column=1, padx=20, pady=20, sticky="nsew")
all_off_button.grid(row=4, column=2, padx=20, pady=20, sticky="nsew")

# Create a label for the author's name
author_label = tk.Label(button_frame, text="Made by Anneshu Nag", font=("Helvetica", 12), fg="white", bg=frame_bg_color)
author_label.grid(row=5, column=0, columnspan=3, padx=20, pady=20)

# Create a grid row for the exit button
button_frame.grid_rowconfigure(5, weight=1)

# Create a grid column for each widget
for i in range(3):
    button_frame.grid_columnconfigure(i, weight=1)

# Run the GUI application
window.mainloop()

# Clean up GPIO on program exit
GPIO.cleanup()
