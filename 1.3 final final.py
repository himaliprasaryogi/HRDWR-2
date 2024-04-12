from machine import Pin, I2C
import time
from ssd1306 import SSD1306_I2C

# Define button pins
up = Pin(9, Pin.IN, Pin.PULL_UP)
clear = Pin(8, Pin.IN, Pin.PULL_UP)
down = Pin(7, Pin.IN, Pin.PULL_UP)

# Initialize I2C interface
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)

# Initialize OLED display
oled = SSD1306_I2C(128, 64, i2c)

# Starting position for line drawing
x = 0
y = 32

# Clear the screen initially
oled.fill(0)
oled.show()

while True:
    # Draw a pixel at current position
    oled.pixel(x, y, 1)
    oled.show()
    
    # Move to the next position
    x += 1
    
    # Wrap around  reaching the right edge
    if x >= 128:
        x = 0
    
    # Check button presses
    if clear.value() == 0:
        # Clear the screen and reset position
        oled.fill(0)
        x = 0
        y = 32
        
    
    if up.value() == 0:
        # Move line up
        if y > 0:
            y -= 1
        
    
    if down.value() == 0:
        # Move line down
        if y < 63:
            y += 1
        
