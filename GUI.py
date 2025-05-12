#!/usr/bin/env python3
"""
Python implementation of the FrontEnd GUI using Tkinter
"""

import tkinter as tk
from tkinter import ttk
import threading
import time
import sys

# import the RibbonCableController
from ribbon_cable_controller import RibbonCableController

class FrontEnd(tk.Tk):
    """
    Main application window for the Ribbon Cable Control Panel
    """
    
    def __init__(self):
        """
        Initialize the application window and components
        """
        super().__init__()
        
        self.title("Ribbon Cable Control Panel")
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        
        # Initialize the ribbon controller
        self.ribbon = RibbonCableController()
        
        # Set up the GUI components
        self.init_components()
    
    def init_components(self):
        """
        Initialize all the GUI components
        """
        # Main frame
        main_frame = ttk.Frame(self, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Left side buttons (L1-L5)
        self.create_button(main_frame, ">", self.l1_pressed, 1, 0)
        self.create_button(main_frame, ">", self.l2_pressed, 2, 0)
        self.create_button(main_frame, ">", self.l3_pressed, 3, 0)
        self.create_button(main_frame, ">", self.l4_pressed, 4, 0)
        self.create_button(main_frame, ">", self.l5_pressed, 5, 0)
        
        # Right side buttons (R1-R5)
        self.create_button(main_frame, "<", self.r1_pressed, 1, 6)
        self.create_button(main_frame, "<", self.r2_pressed, 2, 6)
        self.create_button(main_frame, "<", self.r3_pressed, 3, 6)
        self.create_button(main_frame, "<", self.r4_pressed, 4, 6)
        self.create_button(main_frame, "<", self.r5_pressed, 5, 6)
        
        # Function buttons
        self.create_button(main_frame, "Silence", self.silence_pressed, 6, 0)
        self.create_button(main_frame, "Options", self.options_pressed, 7, 0)
        self.create_button(main_frame, "System On", self.system_on_pressed, 6, 6)
        
        # Up buttons
        self.create_button(main_frame, "^", self.up1_pressed, 8, 1)
        self.create_button(main_frame, "^", self.up2_pressed, 8, 2)
        self.create_button(main_frame, "^", self.up3_pressed, 8, 3)
        self.create_button(main_frame, "^", self.up4_pressed, 8, 4)
        
        # Numeric keypad
        self.create_button(main_frame, "1", self.one_pressed, 9, 1)
        self.create_button(main_frame, "2", self.two_pressed, 9, 2)
        self.create_button(main_frame, "3", self.three_pressed, 9, 3)
        self.create_button(main_frame, "4", self.four_pressed, 10, 1)
        self.create_button(main_frame, "5", self.five_pressed, 10, 2)
        self.create_button(main_frame, "6", self.six_pressed, 10, 3)
        self.create_button(main_frame, "7", self.seven_pressed, 11, 1)
        self.create_button(main_frame, "8", self.eight_pressed, 11, 2)
        self.create_button(main_frame, "9", self.nine_pressed, 11, 3)
        self.create_button(main_frame, "0", self.zero_pressed, 12, 2)
        
        # Navigation buttons
        self.create_button(main_frame, "Up", self.up_arrow_pressed, 9, 5)
        self.create_button(main_frame, "Down", self.down_button_pressed, 10, 5)
        self.create_button(main_frame, "Enter", self.enter_pressed, 11, 5)
        
        # Clear and Cancel buttons
        self.create_button(main_frame, "Clear", self.clear_pressed, 12, 1)
        self.create_button(main_frame, "Cancel", self.cancel_pressed, 12, 3)
        
        # Add some padding to all children of main_frame
        for child in main_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)
    
    def create_button(self, parent, text, command, row, column):
        """
        Helper method to create a button with standard styling
        """
        button = ttk.Button(parent, text=text, command=command)
        button.grid(row=row, column=column)
        return button
    
    def on_close(self):
        """
        Clean up resources when the window is closed
        """
        self.ribbon.shutdown()
        self.destroy()
    
    def toggle_pins(self, pin1, pin2):
        """
        Helper method to toggle a pair of pins on for 200ms then off
        """
        def toggle():
            self.ribbon.set_pin(pin1, True)
            self.ribbon.set_pin(pin2, True)
            time.sleep(0.2)  # 200ms
            self.ribbon.set_pin(pin1, False)
            self.ribbon.set_pin(pin2, False)
        
        # Run the toggle operation in a separate thread to not block the GUI
        threading.Thread(target=toggle).start()
    
    # Button handlers - each toggles specific pins
    
    def one_pressed(self):
        self.toggle_pins(19, 12) #Pin def 8, 19
    
    def two_pressed(self):
        self.toggle_pins(17, 12) #Pin def 12, 19
    
    def three_pressed(self):
        self.toggle_pins(15, 12) #Pin def 20, 19
    
    def four_pressed(self):
        self.toggle_pins(19, 14) #Pin def 8, 21
    
    def five_pressed(self):
        self.toggle_pins(17, 14) #Pin def 12, 21
    
    def six_pressed(self):
        self.toggle_pins(15, 14) #Pin def 20, 21
    
    def seven_pressed(self):
        self.toggle_pins(19, 16) #Pin def 8, 16
    
    def eight_pressed(self):
        self.toggle_pins(17, 16) #Pin def 12, 16
    
    def nine_pressed(self):
        self.toggle_pins(15, 16) #Pin def 20, 16
    
    def zero_pressed(self):
        self.toggle_pins(17, 18) #Pin def 12, 7
    
    def enter_pressed(self):
        self.toggle_pins(13, 16) #Pin def 26, 12
    
    def clear_pressed(self):
        self.toggle_pins(19, 18) #Pin def 8, 7
    
    def cancel_pressed(self):
        self.toggle_pins(13, 18) # Pin def 26,7
    
    def up_arrow_pressed(self):
        self.toggle_pins(13, 12) #Pin def 26, 19
    
    def down_button_pressed(self):
        self.toggle_pins(13, 14) #Pin def 26, 21
    
    def up1_pressed(self):
        self.toggle_pins(3, 4) #Pin def 17, 27
    
    def up2_pressed(self):
        self.toggle_pins(3, 4) #Pin def 17, 27
    
    def up3_pressed(self):
        self.toggle_pins(3, 4) #Pin def 17, 27
    
    def up4_pressed(self):
        self.toggle_pins(3, 4) #Pin def 17, 27
    
    def l1_pressed(self):
        self.toggle_pins(9, 18) #Pin def 5, 7
    
    def l2_pressed(self):
        self.toggle_pins(9, 16) #Pin def 5, 16
    
    def l3_pressed(self):
        self.toggle_pins(9, 14) #Pin def 5, 21
    
    def l4_pressed(self):
        self.toggle_pins(9, 12) #Pin def 5, 19
    
    def l5_pressed(self):
        self.toggle_pins(9, 10) #Pin def 5, 6
    
    def r1_pressed(self):
        self.toggle_pins(11, 18) #Pin def 13, 7
    
    def r2_pressed(self):
        self.toggle_pins(11, 16) #Pin def 13, 16
    
    def r3_pressed(self):
        self.toggle_pins(11, 14) #Pin def 13, 21
    
    def r4_pressed(self):
        self.toggle_pins(11, 12) #Pin def 13, 19
    
    def r5_pressed(self):
        self.toggle_pins(11, 10) #Pin def 6, 13
    
    def system_on_pressed(self):
        self.toggle_pins(1, 0) #Pin def 2,3
    
    def silence_pressed(self):
        self.toggle_pins(3, 4) #Pin def 17, 27
    
    def options_pressed(self):
        self.toggle_pins(3, 4) #Pin def 17, 27


if __name__ == "__main__":
    try:
        app = FrontEnd()
        app.mainloop()
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)