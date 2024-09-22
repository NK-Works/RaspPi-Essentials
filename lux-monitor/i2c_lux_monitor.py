# This code is made by Anneshu Nag, Student ID- 2210994760  #
#                    Dated- 29/09/2023                      #

# Learnt about smbus2 library from -  https://pypi.org/project/smbus2/ #

# Import necessary libraries
import smbus2   # Used to use I2C funstionalities
import time

# Function to read the light sensor and calculate lux value
def read_light_sensor():
    bus = smbus2.SMBus(1)
    data = bus.read_i2c_block_data(0x23, 0x23, 16)  # Default sensor address, default register address, 16-bit value
    raw_value = data[1] + (256 * data[0])
    luxValue = round(raw_value / 1.2, 2)  # Round the lux value to two decimal places
    return luxValue

# Function to classify light intensity based on lux value
def classify_light_intensity(luxValue):
    if luxValue < 10:
        return "Too Dark"
    elif luxValue < 50:
        return "Dark"
    elif luxValue < 500:
        return "Medium"
    elif luxValue > 1000:
        return "Too Bright"
    else:
        return "Bright"

# Display introductory messages
print("\n      -------------------------")
print("      | Light Sensor Readings |")
print("      |   RaspberryPi - I2C   |")
print("      |    -By Anneshu Nag    |")
print("      -------------------------\n")

# Continuous loop for reading and displaying sensor data
while True:
    luxValue = read_light_sensor()
    intensity = classify_light_intensity(luxValue)
    print(f"Light Value: {luxValue:.2f} - Intensity: {intensity}")
    time.sleep(1)
