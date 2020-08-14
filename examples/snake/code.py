import board
from digitalio import DigitalInOut, Pull
from digitalio import DigitalInOut, Direction, Pull
import time
import busio
import adafruit_framebuf
import adafruit_is31fl3731
from random import randint

numbers = [
    [0b0000, 0b0110, 0b1001, 0b1001, 0b1001, 0b1001, 0b1001, 0b0110, 0b0000,],
    [0b0000, 0b0010, 0b0110, 0b0010, 0b0010, 0b0010, 0b0010, 0b0111, 0b0000,],
    [0b0000, 0b0110, 0b1001, 0b1001, 0b0001, 0b0010, 0b0100, 0b1111, 0b0000,],
    [0b0000, 0b0110, 0b1001, 0b0001, 0b0011, 0b0001, 0b1001, 0b0110, 0b0000,],
    [0b0000, 0b0011, 0b0101, 0b1001, 0b1111, 0b0001, 0b0001, 0b0001, 0b0000,],
    [0b0000, 0b1111, 0b1000, 0b1000, 0b1110, 0b0001, 0b0001, 0b1110, 0b0000,],
    [0b0000, 0b0110, 0b1001, 0b1000, 0b0110, 0b1001, 0b1001, 0b0110, 0b0000,],
    [0b0000, 0b1111, 0b0001, 0b0001, 0b0010, 0b0100, 0b0100, 0b1000, 0b0000,],
    [0b0000, 0b0110, 0b1001, 0b1001, 0b0110, 0b1001, 0b1001, 0b0110, 0b0000,],
    [0b0000, 0b0110, 0b1001, 0b1001, 0b0110, 0b0001, 0b1001, 0b0110, 0b0000,],
]

# configure I2C
i2c = busio.I2C(board.SCL, board.SDA)

# turn on LED drivers
sdb = DigitalInOut(board.SDB)
sdb.direction = Direction.OUTPUT
sdb.value = True

# set up the two LED drivers
display = adafruit_is31fl3731.Matrix(i2c, address=0x74)
display2 = adafruit_is31fl3731.Matrix(i2c, address=0x77)


btnA = DigitalInOut(board.BTNA)
btnA.pull = Pull.UP
btnB = DigitalInOut(board.BTNB)
btnB.pull = Pull.UP
btnX = DigitalInOut(board.BTNX)
btnX.pull = Pull.UP
btnY = DigitalInOut(board.BTNY)
btnY.pull = Pull.UP

print(f"screen width: {display.width}")
print(f"screen height: {display.height}")


def spawn_food():
    global food
    food = (randint(0, display.width * 2 - 1), randint(0, display.height - 1))


def set_pixel(pixel, brightness):
    if pixel[0] > display.width - 1:
        display2.pixel(pixel[0] - display.width, pixel[1], brightness)
    else:
        display.pixel(pixel[0], pixel[1], brightness)


def clear():
    display.fill(0)
    display2.fill(0)


def draw_food():
    set_pixel(food, 255)


def move():
    global score
    global last_move
    last_move = time.monotonic()
    prev_head = body[-1]
    if direction == 2:
        head = prev_head[0] % 32, (prev_head[1] - 1) % 9
    elif direction == -2:
        head = prev_head[0] % 32, (prev_head[1] + 1) % 9
    elif direction == 1:
        head = (prev_head[0] + 1) % 32, prev_head[1] % 9
    elif direction == -1:
        head = (prev_head[0] - 1) % 32, prev_head[1] % 9
    # delete tail
    if head == food:
        # food eaten!
        set_pixel(food, 0)
        score += 1
        draw_score()
        spawn_food()
    else:
        # delete tail
        set_pixel(body[0], 0)
        del body[0]
    # DEATH
    if head in body:
        clear()
        exit()

    set_pixel(head, 15)
    body.append(head)


def handle_input():
    global direction
    if not btnA.value:
        if (direction + 2) != 0:
            direction = 2
    elif not btnB.value:
        if (direction - 2) != 0:
            direction = -2
    elif not btnX.value:
        if (direction - 1) != 0:
            direction = -1
    elif not btnY.value:
        if (direction + 1) != 0:
            direction = 1


def bits(n):
    for i in reversed(range(4)):
        yield (2 ** i & n) != 0


def draw_score():
    for offset, digit in enumerate(str(score)):
        number = numbers[int(digit)]
        for y, x_row in enumerate(number):
            for x, brightness in enumerate(bits(x_row)):
                set_pixel((1 + x + offset * 5, y), brightness)


body = [(0, 0)]
# 2 = up, -2 = down, -1 = left, 1 = right
direction = 1
score = 0
frame = False
last_move = time.monotonic()

draw_score()
spawn_food()

while True:
    handle_input()
    time_since_last_move = time.monotonic() - last_move
    if time_since_last_move > 0.2:
        move()
        # draw food everytime
        draw_food()
