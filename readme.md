# Hardware Key Mapping via GPIO for Dirtywave m8 rPi
## Description
This is a simple python script that maps the GPIO pins of a Raspberry Pi to keyboard keys for use with the Dirtywave m8 headless tracker on an rpi4.

See https://github.com/RowdyVoyeur/m8c-rpi4 for details on that project.

### Main Controls
`gpio-hw-keyboard.py` maps the GPIO pins to keyboard keys to control the m8c.

### Volume Up/Down
`gpio-volume-control.py` maps the GPIO pins to volume control buttons.

### Shutdown
`listen-for-shutdown.py` and `listen-for-shutdown.sh` are used to listen for a button press to shutdown the rPi. This is intended to be used with a momentary switch connected to GPIO pin 3 and ground.

Copied from https://github.com/Howchoo/pi-power-button, see instructions there for installation steps.

## Installation
Install the keyboard package at root

```sudo pip3 install keyboard pyalsaaudio```

## Usage

```sudo python3 main.py```