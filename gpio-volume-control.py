import RPi.GPIO as GPIO
import alsaaudio
import time

# Define GPIO pins for the volume up and down buttons
VOLUME_UP_PIN = 23
VOLUME_DOWN_PIN = 24

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(VOLUME_UP_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(VOLUME_DOWN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize the ALSA Mixer control for the USB sound card
mixer = alsaaudio.Mixer(control='Speaker', cardindex=0)

# Define the volume step (adjust as needed)
VOLUME_STEP = 2.5

# Define the delay between volume increments (adjust as needed)
INCREMENT_DELAY = 0.1  # seconds

def volume_up(channel):
    while not GPIO.input(VOLUME_UP_PIN):  # Continue while button is held down
        current_volume = mixer.getvolume()[0]
        new_volume = min(current_volume + VOLUME_STEP, 100)  # Limit to 0-100 range
        mixer.setvolume(new_volume)
        # print(f"Volume up: {new_volume}%")
        time.sleep(INCREMENT_DELAY)

def volume_down(channel):
    while not GPIO.input(VOLUME_DOWN_PIN):  # Continue while button is held down
        current_volume = mixer.getvolume()[0]
        new_volume = max(current_volume - VOLUME_STEP, 0)  # Limit to 0-100 range
        mixer.setvolume(new_volume)
        # print(f"Volume down: {new_volume}%")
        time.sleep(INCREMENT_DELAY)

# Add event detection for button presses
GPIO.add_event_detect(VOLUME_UP_PIN, GPIO.FALLING, callback=volume_up, bouncetime=200)
GPIO.add_event_detect(VOLUME_DOWN_PIN, GPIO.FALLING, callback=volume_down, bouncetime=200)

try:
    # print("Volume control script is running. Press Ctrl+C to exit.")
    while True:
        pass  # Keep the script running

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
