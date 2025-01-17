"""
Type stub for the MicroPython SSD1306 OLED driver.

This library provides a driver for controlling SSD1306 OLED displays over 
I2C or SPI interfaces. It supports basic drawing operations, text rendering, 
and display configuration.

### Usage Examples:

#### SPI Interface:
```python
from machine import Pin, SPI
import ssd1306

spi = SPI(1, baudrate=1000000)
display = ssd1306.SSD1306_SPI(128, 64, spi, dc=Pin(5), res=Pin(2), cs=Pin(4))
display.fill(0)  # Clear the display
display.text("Hello, World!", 0, 0, 1)  # Display text
display.show()
```

#### I2C Interface:
```python
from machine import Pin, I2C
import ssd1306

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.fill(0)  # Clear the display
display.text("Hello, World!", 0, 0, 1)  # Display text
display.show()
```

### Features:
- Supports 128x32 and 128x64 SSD1306 OLED displays.
- Drawing primitives (lines, rectangles, circles, etc.).
- Text rendering.
- Contrast adjustment and screen inversion.

For more details, visit the [SSD1306 GitHub repository](https://github.com/stlehmann/micropython-ssd1306).
"""
# ssd1306.pyi - Stub file for SSD1306 MicroPython library
from typing import Optional
from framebuf import FrameBuffer
from machine import I2C, SPI, Pin

class SSD1306(FrameBuffer):
    """
    Base class for SSD1306 OLED display drivers.
    Provides functionality for rendering graphics and managing the display.
    """
    def __init__(self, width: int, height: int, external_vcc: bool) -> None:
        """
        Initialize the SSD1306 driver.
        
        :param width: Display width in pixels.
        :param height: Display height in pixels.
        :param external_vcc: Whether to use external VCC (True) or internal (False).
        """
        ...

    def init_display(self) -> None:
        """Initialize and configure the display for operation."""
        ...

    def poweroff(self) -> None:
        """Turn off the display."""
        ...

    def poweron(self) -> None:
        """Turn on the display."""
        ...

    def contrast(self, contrast: int) -> None:
        """
        Set the display contrast level.
        
        :param contrast: Contrast value (0-255).
        """
        ...

    def invert(self, invert: bool) -> None:
        """
        Invert the display colors.
        
        :param invert: True to invert colors, False to return to normal.
        """
        ...

    def show(self) -> None:
        """
        Refresh the display with the current buffer content.
        Ensures all data is displayed on the screen.
        """
        ...


class SSD1306_I2C(SSD1306):
    """
    SSD1306 driver for I2C communication.
    Manages interaction with the display using the I2C protocol.
    """
    def __init__(self, width: int, height: int, i2c: I2C, addr: int = 0x3C, external_vcc: bool = False) -> None:
        """
        Initialize the SSD1306 I2C driver.
        
        :param width: Display width in pixels.
        :param height: Display height in pixels.
        :param i2c: I2C object for communication.
        :param addr: I2C address of the display.
        :param external_vcc: Whether to use external VCC (True) or internal (False).
        """
        ...

    def write_cmd(self, cmd: int) -> None:
        """
        Write a command to the display via I2C.
        
        :param cmd: Command byte to send.
        """
        ...

    def write_data(self, buf: bytes) -> None:
        """
        Write data to the display via I2C.
        
        :param buf: Data buffer to send.
        """
        ...


class SSD1306_SPI(SSD1306):
    """
    SSD1306 driver for SPI communication.
    Manages interaction with the display using the SPI protocol.
    """
    def __init__(self, width: int, height: int, spi: SPI, dc: Pin, res: Pin, cs: Pin, 
                 external_vcc: bool = False) -> None:
        """
        Initialize the SSD1306 SPI driver.
        
        :param width: Display width in pixels.
        :param height: Display height in pixels.
        :param spi: SPI object for communication.
        :param dc: Data/Command control pin.
        :param res: Reset pin.
        :param cs: Chip Select pin.
        :param external_vcc: Whether to use external VCC (True) or internal (False).
        """
        ...

    def write_cmd(self, cmd: int) -> None:
        """
        Write a command to the display via SPI.
        
        :param cmd: Command byte to send.
        """
        ...

    def write_data(self, buf: bytes) -> None:
        """
        Write data to the display via SPI.
        
        :param buf: Data buffer to send.
        """
        ...
