# RaspPi-Essentials

Welcome to **RaspPi-Essentials**, a collection of essential Raspberry Pi projects for beginners and enthusiasts. This repository demonstrates key Raspberry Pi functionalities such as controlling LEDs, reading light sensor data, generating PWM signals, and working with Morse code signals.

## Projects Overview

### 1. Light Sensor Readings using I2C
- **File:** `i2c_lux_monitor.py`
- **Description:** This script communicates with a light sensor over the I2C protocol to read and display ambient light levels (lux). It demonstrates how to interface with an external sensor using the Raspberry Pi’s I2C bus.

### 2. LED Control Panel using GUI
- **File:** `led_control_panel.py`
- **Description:** A graphical interface for controlling the brightness and state of LEDs connected to the Raspberry Pi’s GPIO pins. This project highlights the use of a simple GUI to interact with hardware components.

### 3. Morse Code Signaling with LEDs
- **File:** `morse_signal_gui.py`
- **Description:** This project translates text into Morse code and blinks an LED according to the Morse pattern. The user can input messages via a graphical interface, and the Raspberry Pi controls the LED to display the Morse signals.

### 4. PWM Control on Raspberry Pi
- **File:** `pi_pwm_control.py`
- **Description:** This script demonstrates Pulse Width Modulation (PWM) on the Raspberry Pi, allowing precise control over components like motors or LEDs by adjusting duty cycles and frequencies in real-time.

## Requirements

- Raspberry Pi with GPIO access
- Python 3.x
- I2C-enabled light sensor (e.g., BH1750, TSL2561)
- LEDs and resistors
- GUI framework (Tkinter)
- RPi.GPIO or other GPIO libraries for Raspberry Pi

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/NK-Works/RaspPi-Essentials.git
