# Hardware Key Mapping via GPIO for Dirtywave m8 rPi
## Description
This is a simple python script that maps the GPIO pins of a Raspberry Pi to keyboard keys for use with the Dirtywave m8 headless tracker on an rpi4.

See https://github.com/RowdyVoyeur/m8c-rpi4 for details on that project.

### Main Controls
`gpio-hw-keyboard.py` maps the GPIO pins to keyboard keys to control the m8c.
```
26: "up",
19: "right",
13: "down",
6: "left",
21: "a", #option
20: "s", #edit
16: "z", #shift
12: "x", #play
```

### Volume Up/Down
`gpio-volume-control.py` maps the GPIO pins to volume control buttons.

```
23: Volume Up
24: Volume Down
```


### Shutdown
`listen-for-shutdown.py` and `listen-for-shutdown.sh` are used to listen for a button press to shutdown the rPi. This is intended to be used with a momentary switch connected to GPIO pin 3 and ground.

Copied from https://github.com/Howchoo/pi-power-button, see instructions there for installation steps.

## Installation
Install required packages at root

```
sudo pip3 install keyboard pyalsaaudio
```

Copy the service file to systemd

```
sudo cp ~/m8c-rpi-gpio/m8c-rpi-gpio.service /etc/systemd/system/m8c-rpi-gpio.service
```

Enable and start the service

```
sudo systemctl daemon-reload
```

```
sudo systemctl enable m8c-rpi-gpio.service
```

```
sudo systemctl start m8c-rpi-gpio.service
```

## Usage

```
sudo python3 main.py
```
