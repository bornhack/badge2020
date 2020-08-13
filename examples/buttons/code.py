import board
from digitalio import DigitalInOut, Pull

# Digital inputs are input by default so there is no need to specify a direction
# The button pins do need to be pulled up using the pull-up resistor built into the SAMD microcontroller

btnA = DigitalInOut(board.BTNA)
btnA.pull = Pull.UP
btnB = DigitalInOut(board.BTNB)
btnB.pull = Pull.UP
btnX = DigitalInOut(board.BTNX)
btnX.pull = Pull.UP
btnY = DigitalInOut(board.BTNY)
btnY.pull = Pull.UP

# You can read the value by looking at the variable "btnA.value", this boolean will be False when the button is being pressed
# and True when the button is not being pressed

oldA = True
oldB = True
oldX = True
oldY = True

while True:
    newA = btnA.value
    newB = btnB.value
    newX = btnX.value
    newY = btnY.value

    if newA != oldA:
        oldA = newA
        if not newA:
            print("Button A pressed!")
        else:
            print("Button A released!")

    if newB != oldB:
        oldB = newB
        if not newB:
            print("Button B pressed!")
        else:
            print("Button B released!")

    if newX != oldX:
        oldX = newX
        if not newX:
            print("Button X pressed!")
        else:
            print("Button X released!")

    if newY != oldY:
        oldY = newY
        if not newY:
            print("Button Y pressed!")
        else:
            print("Button Y released!")
