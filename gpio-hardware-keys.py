import RPi.GPIO as GPIO
import time
import keyboard

class ButtonToKeyMapper:
    def __init__(self, button_key_mappings):
        self.button_key_mappings = button_key_mappings
        self.button_states = {pin: False for pin in button_key_mappings.keys()}

        # Initialize GPIO and setup pins
        GPIO.setmode(GPIO.BCM)
        for button_pin in self.button_key_mappings:
            GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def monitor_buttons(self):
        try:
            while True:
                for button_pin, key in self.button_key_mappings.items():
                    button_state = not GPIO.input(button_pin)  # Invert the logic because PUD_UP is used
                    if button_state:
                        if not self.button_states[button_pin]:
                            # Button is pressed for the first time
                            keyboard.press(key)
                            self.button_states[button_pin] = True
                            # print("Button pressed: " + key)
                    else:
                        if self.button_states[button_pin]:
                            # Button is released
                            keyboard.release(key)
                            self.button_states[button_pin] = False

                    # You can add additional keypresses or logic here as needed.

                # Add a slight delay to debounce the buttons (adjust as needed)
                time.sleep(0.05)

        except KeyboardInterrupt:
            pass

        finally:
            # Release any keys that may still be held down
            for key in self.button_key_mappings.values():
                keyboard.release(key)
            GPIO.cleanup()

# Define GPIO pin to key mappings (adjust as needed)
button_key_mappings = {
    26: "up",  # Use the key string instead of Key.space
    19: "right",  # Use the key string instead of Key.enter
    13: "down",
    6: "left",
    21: "a", #option
    20: "s", #edit
    16: "z", #shift
    12: "x", #play
}

# Create an instance of the ButtonToKeyMapper class
button_mapper = ButtonToKeyMapper(button_key_mappings)

# Start monitoring the buttons
button_mapper.monitor_buttons()
