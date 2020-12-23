# H6

A Python library to emulate a Zoom H6 recorder remote control

## Introduction

This library allows you to control your Zoom H6 recorder from your computer using an USB to TTL adapter.
For this, you will need a few components to make a specific cable, but it's quite simple.

## Cable

You will have to make a specific cable that connects a USB port from your computer to the Zoom H6 remote control port, but fear not. It's actually really simple.

You will need:

- An FTDI USB to TTL converter:

![FTDI USB to TTL](images/FT232RL-FTDI-USB-to-TTL.jpeg?raw=true "FTDI USB to TTL")

- A 2.5mm jack screw terminal:

![2.5mm jack screw terminal](images/2-5mm-Stereo-Jack.jpeg?raw=true "2.5mm jack screw terminal")

- A simple 3 wire cable

All of these components are widely available to buy online and the overall cost is less than 5€.

Once you have all of the components, the wiring is also quite simple:

| FTDI adapter | 2.5mm jack |
|--------------|------------|
| Rx           | L          |
| Tx           | R          |
| GND          | V          |

![Wiring](images/wiring.jpeg?raw=true "Wiring")

**IMPORTANT**: Make sure that the FTDI USB to TTL adapter jumper is set to **3.3v** before using the cable. Leaving it at 5v could damage your recorder.

## Installation

Simply install the library using `pip`:

`pip install h6`

## Usage

You can include this library in your Python project or run it directly as a CLI tool.

### CLI

To execute commands using your command line run:

`h6 -p /dev/cu.usbserial-alcdut1 -c stop`

You must specify the serial port using `-p` or `--port` and the command to send using `-c` or `--command`.

### Importing the library

Usage example:

``` python
from h6 import ZoomH6
from time import sleep

# Define the serial port
serial_port = '/dev/cu.usbserial-alcdut1'

# Instantiate recorder
recorder = ZoomH6(serial_port)

# Initialize recorder
recorder.initialize()

# Send 'rec' command
recorder.send('record')

# wait for a while
sleep(3)

# Send 'stop' command
recorder.send('stop')
```

As you can see, when instantiating the ZoomH6 class you will need to specify the serial port where your FTDI USB to TTL adapter is connected.

The `initialize()` function executes a specific handshake expected by the Zoom H6 recorder in order to accept incoming commands.

You can send any valid command to the recorder. Keep reading for a list with all the available commands.

## Commands

The complete list of available commands is:

| Command           | Button            |
|-------------------|-------------------|
| play_pause        | Play / Pause      |
| stop              | Stop              |
| record            | Record            |
| forward           | Forward           |
| reverse           | Reverse           |
| vol_up            | Increase volume   |
| vol_down          | Decrease volume   |
| ch1               | Toggle Channel 1  |
| ch2               | Toggle Channel 2  |
| ch3               | Toggle Channel 3  |
| ch4               | Toggle Channel 4  |
| right             | Right             |
| left              | Left              |

## Changelog

- **0.1.0**: Initial release
