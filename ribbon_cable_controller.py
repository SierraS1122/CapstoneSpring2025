#!/usr/bin/env python3
"""
RibbonCableController for controlling a 20-pin ribbon cable
using Raspberry Pi GPIO pins via RPi.GPIO library

This version includes a mock GPIO module that can be used for testing
on non-Raspberry Pi systems.
"""

import time
import sys

# Try to import RPi.GPIO, and if it fails, use a mock version
try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    # Create a mock GPIO module for testing on non-Raspberry Pi systems
    class MockGPIO:
        BCM = "BCM"
        OUT = "OUT"
        IN = "IN"
        HIGH = True
        LOW = False
        
        @staticmethod
        def setmode(mode):
            print(f"[MOCK] GPIO.setmode({mode})")
            
        @staticmethod
        def setwarnings(flag):
            print(f"[MOCK] GPIO.setwarnings({flag})")
            
        @staticmethod
        def setup(channel, mode):
            print(f"[MOCK] GPIO.setup(channel={channel}, mode={mode})")
            
        @staticmethod
        def output(channel, state):
            print(f"[MOCK] GPIO.output(channel={channel}, state={state})")
            
        @staticmethod
        def cleanup():
            print("[MOCK] GPIO.cleanup()")
    
    # Use the mock GPIO
    GPIO = MockGPIO
    print("Running with mock GPIO for testing (not on a Raspberry Pi)")


class RibbonCableController:
    """
    Simple RibbonCableController for controlling a 20-pin ribbon cable
    using Raspberry Pi GPIO pins via RPi.GPIO library
    """
    
    # Pin definitions (using BCM pin numbering)
    PIN_DEFINITIONS = [
        2, 3, 4, 17, 27,   # Pins 1-5
        22, 10, 9, 11, 5,  # Pins 6-10
        6, 13, 19, 26, 21, # Pins 11-15
        20, 16, 12, 7, 8   # Pins 16-20
    ]
    
    def __init__(self):
        """
        Constructor - initializes GPIO controller and sets up pins
        """
        # Set up GPIO using BCM numbering
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        # Set up all pins as digital outputs (initially LOW/closed)
        for pin in self.PIN_DEFINITIONS:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
        
        print(f"Ribbon cable controller initialized with {len(self.PIN_DEFINITIONS)} pins")
    
    def set_pin(self, pin_index, state):
        """
        Set a single pin to HIGH (open) or LOW (closed)
        
        Args:
            pin_index: index of the pin (0-19)
            state: True for HIGH/open, False for LOW/closed
        """
        if 0 <= pin_index < len(self.PIN_DEFINITIONS):
            pin = self.PIN_DEFINITIONS[pin_index]
            gpio_state = GPIO.HIGH if state else GPIO.LOW
            GPIO.output(pin, gpio_state)
            print(f"Pin {pin_index} set to {'HIGH/open' if state else 'LOW/closed'}")
        else:
            print(f"Error: Pin index {pin_index} is out of range (0-19)", file=sys.stderr)
    
    def set_all_pins(self, states):
        """
        Set all pins according to a list of states
        
        Args:
            states: list of boolean values (True for HIGH/open, False for LOW/closed)
        """
        if len(states) != len(self.PIN_DEFINITIONS):
            print(f"Error: Expected {len(self.PIN_DEFINITIONS)} states, got {len(states)}", file=sys.stderr)
            return
        
        for i, state in enumerate(states):
            pin = self.PIN_DEFINITIONS[i]
            gpio_state = GPIO.HIGH if state else GPIO.LOW
            GPIO.output(pin, gpio_state)
        
        print("All pins set according to provided states")
    
    def set_pattern(self, pattern):
        """
        Set pins according to a binary pattern string
        
        Args:
            pattern: String of 20 '1's and '0's ('1' for HIGH/open, '0' for LOW/closed)
        """
        if len(pattern) != len(self.PIN_DEFINITIONS):
            print(f"Error: Expected pattern of length {len(self.PIN_DEFINITIONS)}, got {len(pattern)}", file=sys.stderr)
            return
        
        states = [c == '1' for c in pattern]
        self.set_all_pins(states)
    
    def shutdown(self):
        """
        Clean up GPIO resources
        """
        GPIO.cleanup()
        print("GPIO resources cleaned up")


if __name__ == "__main__":
    controller = None
    
    try:
        controller = RibbonCableController()
        
        # Example: Set individual pins
        controller.set_pin(0, True)   # Set first pin HIGH/open
        controller.set_pin(19, True)  # Set last pin HIGH/open
        time.sleep(1)
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
    finally:
        # Clean up
        if controller:
            controller.shutdown()