import board
import time
from digitalio import DigitalInOut, Direction, Pull
import busio
import adafruit_framebuf
import adafruit_is31fl3731

# configure I2C
i2c = busio.I2C(board.SCL, board.SDA)

# turn on LED drivers
sdb = DigitalInOut(board.SDB)
sdb.direction = Direction.OUTPUT
sdb.value = True

# set up the two LED drivers
display = adafruit_is31fl3731.Matrix(i2c, address=0x74)
display2 = adafruit_is31fl3731.Matrix(i2c, address=0x77)

text_to_show = "BornHack 2020 - make clean"
 
# Create a framebuffer for our display
buf = bytearray(64)  # 2 bytes tall x 32 wide = 64 bytes (9 bits is 2 bytes)
fb = adafruit_framebuf.FrameBuffer(
    buf, display.width*2, display.height, adafruit_framebuf.MVLSB
)

frame = 0  # start with frame 0
while True:
    for i in range(len(text_to_show) * 9):
        fb.fill(0)
        fb.text(text_to_show, -i*2 + display.width*2, 1, color=1)
 
        # to improve the display flicker we can use two frame
        # fill the next frame with scrolling text, then
        # show it.
        display.frame(frame, show=False)
        display2.frame(frame, show=False)
        # turn all LEDs off
        display.fill(0)
        display2.fill(0)
        for x in range(display.width):
            # using the FrameBuffer text result
            bite = buf[x]
            for y in range(display.height):
                bit = 1 << y & bite
                # if bit > 0 then set the pixel brightness
                if bit:
                    display.pixel(x, y, 30)
 
        for x in range(display2.width):
            # using the FrameBuffer text result
            bite = buf[x+16]
            for y in range(display2.height):
                bit = 1 << y & bite
                # if bit > 0 then set the pixel brightness
                if bit:
                    display2.pixel(x, y, 30)
 
        # now that the frame is filled, show it.
        display.frame(frame, show=True)
        display2.frame(frame, show=True)
        frame = 0 if frame else 1
