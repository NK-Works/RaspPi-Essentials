# This code is written by Anneshu Nag, Student ID- 2210994760 #
#                       Dated- 16/09/2023                     #
#    Blinking Morse Codes through Raspberry Pi using GUI      #

# Importing the necessary libraries to create the program
import RPi.GPIO as GPIO
import time
import tkinter as tk
import threading

# Define GPIO pin for the LED
LED_PIN = 14

# Morse Codes dictionary
my_morse_codes = {
    'A': '.-', 
    'B': '-...', 
    'C': '-.-.', 
    'D': '-..', 
    'E': '.',
    'F': '..-.', 
    'G': '--.', 
    'H': '....', 
    'I': '..', 
    'J': '.---',
    'K': '-.-', 
    'L': '.-..', 
    'M': '--', 
    'N': '-.', 
    'O': '---',
    'P': '.--.', 
    'Q': '--.-', 
    'R': '.-.', 
    'S': '...', 
    'T': '-',
    'U': '..-', 
    'V': '...-', 
    'W': '.--', 
    'X': '-..-', 
    'Y': '-.--',
    'Z': '--..', 
    ' ': '/'
}

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Function to blink Morse code
def bink_morse_func(letter):
    if letter in my_morse_codes:
        morse_code = my_morse_codes[letter]
        for symbol in morse_code:
            if symbol == '.':
                GPIO.output(LED_PIN, GPIO.HIGH)
                time.sleep(0.2)  # Duration for dot
                GPIO.output(LED_PIN, GPIO.LOW)
                time.sleep(0.2)  # Pause between symbols
            elif symbol == '-':
                GPIO.output(LED_PIN, GPIO.HIGH)
                time.sleep(0.6)  # Duration for dash (3x dot)
                GPIO.output(LED_PIN, GPIO.LOW)
                time.sleep(0.2)  # Pause between symbols (1x dot)
            else:
                # Pause between words (for space)
                time.sleep(1.4)  # 7x dot
        # Pause between letters
        time.sleep(0.6) # 3x dot

# Function to handle when the button enter is pressed
def entering_morse_blink():
    user_input = entry.get().upper()
    message_label.config(text="", bg="lightyellow")  # Clear any previous messages
    if user_input:
        if len(user_input) <= 12:
            if not any(char.isdigit() for char in user_input):
                message_label.config(text=f"Blinking for: {user_input}", fg="darkgreen", bg="lightyellow")
                blinking_in_progress[0] = True
                
                def blinker_thread():
                    for letter in user_input:
                        if letter in my_morse_codes:
                            bink_morse_func(letter)
                    message_label.config(text="Blink completed.", fg="darkgreen", bg="lightyellow")
                    entry.delete(0, 'end')  # Clear the entry field
                    window.after(2000, lambda: message_label.config(text=""))  # Clear message after a delay
                    blinking_in_progress[0] = False
                    error_label.config(text="Press Exit to Close Window.", fg="green")
                    window.after(2000, lambda: error_label.config(text=""))
                    
                # Start the blinking thread
                threading.Thread(target=blinker_thread).start()
            else:
                message_label.config(text="Numerical Entries - Invalid!", fg="red", bg="lightyellow")
                entry.delete(0, 'end')  
                window.after(2000, lambda: message_label.config(text=""))  
        else:
            message_label.config(text="Input is Too Long.", fg="red", bg="lightyellow")
            entry.delete(0, 'end')  
            window.after(2000, lambda: message_label.config(text=""))  
    else:
        message_label.config(text="Please Enter Text.", fg="red", bg="lightyellow")
        entry.delete(0, 'end')  
        window.after(2000, lambda: message_label.config(text=""))  

# Function to exit the application
def close_window():
    if blinking_in_progress[0]:
        error_label.config(text="Morse is not Complete! Wait...", fg="red")
    else:
        GPIO.cleanup()
        window.destroy()

# Create the main window
window = tk.Tk()
window.title("RPi Morse GUI")
window.geometry("500x380")
window.configure(bg="lightyellow")

# Create a frame to contain the heading and other widgets in the row
header_frame = tk.Frame(window, bg="black")
header_frame.pack(fill="x") 

# Create an introductory label with spacing
title_label = tk.Label(header_frame, text="NK-Works - RPi Morse GUI", font=("Helvetica", 24, "bold"), fg="white", bg="black")
title_label.pack(anchor="center", pady=(20, 0))

intro_label = tk.Label(window, text="Enter Text (Max. 12 Chars)", font=("Helvetica", 20, "bold"), fg="darkblue", bg= "lightyellow")
intro_label.pack(anchor="center", pady=(20, 0))

# Create a label to display messages
message_label = tk.Label(window, text="", font=("Helvetica", 16), bg="lightyellow")
message_label.pack(anchor="center", pady=(10, 0))

# Create an entry field
entry = tk.Entry(window, width=25, font=("Helvetica", 16), bd=2, relief="ridge")
entry.pack(anchor="center", pady=(20, 0))

# Create a label to display messages
error_label = tk.Label(window, text="", font=("Helvetica", 16), bg="lightyellow")
error_label.pack(anchor="center", pady=(10, 0))

# Create a blink button with increased size and green color
blink_button = tk.Button(window, text="ENTER", command=entering_morse_blink, font=("Helvetica", 12, "bold"), width=10, height=2, bg="green", fg="white")
blink_button.pack(side="left", padx=(50, 10))

# Create an exit button with increased size and red color
exit_button = tk.Button(window, text="EXIT", command=close_window, font=("Helvetica", 12, "bold"), width=10, height=2, bg="red", fg="white")
exit_button.pack(side="right", padx=(10, 50))

# Create a label at the bottom with spacing using grid
bottom_label = tk.Label(window, text="Made by Anneshu Nag", pady=10, font=("Helvetica", 10, "italic", "bold"), bg="lightyellow")
bottom_label.pack(side=tk.BOTTOM, anchor="center")

blinking_in_progress = [False]

# Run the Tkinter main loop
window.mainloop()
