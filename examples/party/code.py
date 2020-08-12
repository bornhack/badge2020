import board, time, busio, adafruit_is31fl3731
from digitalio import DigitalInOut, Direction, Pull
import adafruit_framebuf

brightness = 40

i2c = busio.I2C(board.SCL, board.SDA)
sdb = DigitalInOut(board.SDB)
sdb.direction = Direction.OUTPUT
sdb.value = True
display1 = adafruit_is31fl3731.Matrix(i2c, address=0x74)
display2 = adafruit_is31fl3731.Matrix(i2c, address=0x77)

buf = bytearray(64)  # 2 bytes tall x 32 wide = 64 bytes (9 bits is 2 bytes)
fb = adafruit_framebuf.FrameBuffer(
    buf, display1.width*2, display1.height, adafruit_framebuf.MVLSB
)

def blit(frame):
	display1.frame(frame, show=False)
	display2.frame(frame, show=False)
	for x in range(display1.width):
		bite = buf[x]
		for y in range(display1.height):
			bit = 1 << y & bite
			if bit:
				display1.pixel(x, y, brightness)
		bite = buf[x+16]
		for y in range(display2.height):
			bit = 1 << y & bite
			if bit:
				display2.pixel(x, y, brightness)

def show(frame):
	display1.frame(frame, show=True)
	display2.frame(frame, show=True)

def flash(a,b):
	show(0)
	display1.fill(brightness if a else 0)
	display2.fill(brightness if b else 0)

display1.frame(0, show=False)
display1.frame(0, show=False)
display1.fill(0)
display2.fill(0)

fb.fill(0)
fb.text("PARTY", 0, 1, color=1)
blit(1)

fb.fill(0)
fb.text("HARD!", 0, 1, color=1)
blit(2)

fb.fill(0)
fb.text("CYBER", 0, 1, color=1)
blit(3)

while True:
	for i in range(4):
		flash(True,False)
		time.sleep(0.4/(i+1))
		flash(False,True)
		time.sleep(0.4/(i+1))
		flash(False,False)
		time.sleep(0.4/(i+1))
		flash(True,True)
		time.sleep(0.4/(i+1))
		flash(False,False)
		time.sleep(0.4/(i+1))
		flash(True,True)
		time.sleep(0.4/(i+1))
	
	for i in range(4):
		show(1)
		time.sleep(0.1)
		flash(False,False)
		time.sleep(0.1)
		
	for i in range(4):
		show(2)
		time.sleep(0.1)
		flash(False,False)
		time.sleep(0.1)

	for i in range(4):
		flash(True,False)
		time.sleep(0.4/(i+1))
		flash(False,True)
		time.sleep(0.4/(i+1))
		flash(False,False)
		time.sleep(0.4/(i+1))
		flash(True,True)
		time.sleep(0.4/(i+1))
		flash(False,False)
		time.sleep(0.4/(i+1))
		flash(True,True)
		time.sleep(0.4/(i+1))
		
	for i in range(8):
		show(3)
		time.sleep(0.1)
		flash(False,False)
		time.sleep(0.1)
