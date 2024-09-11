# This code is written by Anneshu Nag, Student ID- 2210994760 #
#                       Dated- 23/09/2023                     #
#  Using Ultrasonic Sensor to glow LED at variable intensity  #
#    Playing the buzzer at different frequency accordingly    #

# Learnt all about gpiozero from: https://gpiozero.readthedocs.io/en/stable/index.html # 

# Importing the gpiozreo library 
from gpiozero import DistanceSensor, PWMLED, PWMOutputDevice # For Buzzer
from time import sleep

# Set the GPIO pin numbers for the ultrasonic sensor, LED, and buzzer
TRIG_PIN = 23
ECHO_PIN = 24  
LED_PIN = 14   
BUZZER_PIN = 15  

# Create a DistanceSensor object for the ultrasonic sensor
ultrasonic_sensor = DistanceSensor(echo=ECHO_PIN, trigger=TRIG_PIN, max_distance = 0.5)

# Create a PWMLED object for the LED
led = PWMLED(LED_PIN)

# Create a PWMBuzzer object for the buzzer (Innate PWM for buzzer is not there so used PWMOutputDevice get the desired effects)
buzzer = PWMOutputDevice(BUZZER_PIN)

# Some Introductory messages
print("\n----NK-WORKS----")
print("| Learning PWM |")
print("|By Anneshu Nag|")
print("----------------")

try:
    while True:
        sleep(1)
        distance = ultrasonic_sensor.distance
        print("Distance (in CM): %.2f" % (distance*100))
        
        # Calculate the optimum distance to brightness ratio (calculated manually for my setup)
        brightness_pitchVal = 1.0 if distance < 0.1 else 1.0 - (distance - 0.1) / 0.4
        
        print ("LED Brightness: %.2f" % brightness_pitchVal)
        # Valid brigtness is between 0 and 1
        led.value = brightness_pitchVal
        
        print("Buzzer Pitch: %.2f" % brightness_pitchVal)
        # Valid pitch is between 0 and 1
        buzzer.value = brightness_pitchVal
        
        print("")

except KeyboardInterrupt:
    # Clean up GPIO
    buzzer.stop()
    GPIO.cleanup()
