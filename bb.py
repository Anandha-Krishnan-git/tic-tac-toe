#updated code 

import Adafruit_MCP230XX
import RPi.GPIO as GPIO
import time

# Initialize MCP23017
mcp = Adafruit_MCP230XX.Adafruit_MCP230XX(address=0x20)

# Define MCP23017 GPIO pins
TOUCH_SENSOR_PINS_MCP = list(range(0, 8))  # GPIO pins 0-7 for Touch Sensors
MCP_LED_PINS = list(range(8, 16))          # GPIO pins 8-15 for MCP23017 LEDs

# Define Raspberry Pi GPIO pins
PI_TOUCH_SENSOR_PIN = 4  # GPIO pin for 1 Raspberry Pi Touch Sensor
PI_LED_PINS = [17, 27, 22, 5, 6, 13, 19, 26, 12, 23]  # GPIO pins for Raspberry Pi LEDs

# Set up MCP23017 GPIOs
for pin in MCP_LED_PINS:
    mcp.setup(pin, Adafruit_MCP230XX.GPIO.OUT)

for pin in TOUCH_SENSOR_PINS_MCP:
    mcp.setup(pin, Adafruit_MCP230XX.GPIO.IN)

# Set up Raspberry Pi GPIOs
GPIO.setmode(GPIO.BCM)
GPIO.setup(PI_TOUCH_SENSOR_PIN, GPIO.IN)
for pin in PI_LED_PINS:
    GPIO.setup(pin, GPIO.OUT)

def set_mcp_led(pin, state):
    mcp.output(pin, state)

def set_pi_led(pin, state):
    GPIO.output(pin, state)

def read_mcp_sensor(pin):
    return mcp.input(pin)

def read_pi_sensor():
    return GPIO.input(PI_TOUCH_SENSOR_PIN)

def main():
    try:
        while True:
            # Read MCP23017 touch sensors
            for i in TOUCH_SENSOR_PINS_MCP:
                if read_mcp_sensor(i) == 1:
                    print(f"Touch detected on MCP sensor {i}")
                    # Turn on the corresponding MCP23017 LED
                    set_mcp_led(MCP_LED_PINS[i-8], 1)
                    time.sleep(1)  # Debounce delay
                    set_mcp_led(MCP_LED_PINS[i-8], 0)
            
            # Read Raspberry Pi touch sensor
            if read_pi_sensor() == 1:
                print("Touch detected on Raspberry Pi sensor")
                # Example action: Turn on one of the Raspberry Pi LEDs
                for pin in PI_LED_PINS:
                    set_pi_led(pin, 1)
                    time.sleep(0.5)
                    set_pi_led(pin, 0)
                    time.sleep(0.5)

    except KeyboardInterrupt:
        print("Exiting...")
        GPIO.cleanup()
        # Cleanup MCP23017 if necessary

if __name__ == "__main__":
    main()
