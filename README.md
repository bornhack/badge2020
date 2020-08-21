# Bornhack Badge 2020

## About the hardware

Similar to the last couple of years, this badge has an ARM cortex M0+ as the main
controller, but on this badge it's the SAMD21 from Microchip, with 4 times as much
flash and RAM compared to the chips from the previous badges.

This makes it possible to run Adafruit CircuitPython on this badge, which lowers the
bar for how easy it is to get started hacking on the badge, since all you need is a
USB cable to connect it to your computer and an editor (vi, nano, VSCode, notepad,
you name it) to change the `code.py` file on the badge. No need to have a tool chain
installed on your computer, it's all happening on the badge when you save the file.

## Features

- The main feature of the badge is a 9x32 pixel LED matrix controlled by 2
IS31FL3731 LED controllers, that control the LEDs via charlieplexing
- The other primary feature is an infrared LED to transmit and an infrared receiver
and decoder to receive badge to badge communication
- There are also 4 navigation/game buttons and a reset button
- The badge is either powered by 2xAA batteries, that have the voltage boosted to
3.3v or via USB, where the voltage is regulated down to 3.3v
- The main controller is a SAMD21G18A with a GD25Q32C (4MB SPI flash) connected
for libraries, graphics, etc.
- There is also an unpopulated header for Shitty Add On v.1.69bis
- On the back of the badge, all i/o pins that are not used on the microcontroller
is pull out to small SMD pads for optional soldering on add-ons or similar.

## Getting started

To start making your badge your own, you can connect it via USB and a mass storage
device should show up with a `code.py` file in the root directory.

If you open that file in your favorite text editor you will find a few lines first
that loads some libraries, then some initialisation of the LED drivers and on line 20
you will find an assignment of a string variable with the scrolling text shown on
the LED matrix. To put eg. your name on the badge, you can change this text and save
the file, and after a few seconds, the badge will restart the code and your text
should be slowly scrolling across the "screen".

If you have gotten this far you are up and running with your first "hack" of the
2020 BornHack badge and you can continue with more elaborate hacking.

## Projects 

- [Generative animations using OCaml](https://github.com/rand00/bornhack2020-badge_generative-animations)


