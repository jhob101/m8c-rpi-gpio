#!/usr/bin/env python

import RPi.GPIO as GPIO
import subprocess
import time

SHUTDOWN_PIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(SHUTDOWN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    GPIO.wait_for_edge(SHUTDOWN_PIN, GPIO.FALLING)

    # Wait for 1 second to check if the button is still pressed
    time.sleep(1)

    if not GPIO.input(SHUTDOWN_PIN):  # If the button is still pressed after 1 second
        subprocess.call(['shutdown', '-h', 'now'], shell=False)
