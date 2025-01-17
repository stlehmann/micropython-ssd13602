# micropython-ssd1306
This is a fork of the driver for SSD1306 displays which is hosted in the
[Micropython package](https://github.com/micropython/micropython). The purpose
of this fork is to make the driver available on PyPi and thus installable via
the upip package manager.

## Installation
Use the upip package manager:

    upip.install('micropython-ssd1306')

If your board or your computer doesn't have an active internet connection you
can also clone this project on your local drive and copy the *ssd1306.py* to
your board.

## Type Stubs for IDE Support
This library now includes `.pyi` type stubs for better IDE integration. To enable autocomplete and type checking in VS Code or other editors:
- Ensure the `.pyi` files are in your project directory or accessible in your Python path.
- If needed, add the directory to your IDE's settings (e.g., `python.analysis.extraPaths` in VS Code).
- If you are using a virtual environment, ensure the stubs are installed in the virtual environment.

## Example Usage
This shows an example usage on an *ESP32* board with an *SSD1306* display
with an resolution of 128x32 pixels. The display is connected via I2C. On the
*ESP32* the I2C pins are: SDA: 23, SCL: 22.

First we set up the I2C bus on our *ESP32* and scan for devices.

    >>> import machine
    >>> i2c = machine.I2C(sda=machine.Pin(23), scl=machine.Pin(22))
    >>> i2c.scan()
    [60]

This shows us that there is a device on address 60 which is 3C in Hex. That is
where our display is supposed to live. Now we create an object for our OLED
display.

    >>> from ssd1306 import SSD1306_I2C
    >>> oled = SSD1306_I2C(128, 32, i2c)

This is it. Now we can use our OLED display:

    >>> oled.fill(1)
    >>> oled.show()

This fills the whole display with white pixels. To clear the display do:

    >>> oled.fill(0)
    >>> oled.show()

Now we can also write some text:

    >>> oled.text('Hello', 0, 0)
    >>> oled.text('World', 0, 10)
    >>> oled.show()

Find more information on how to use the SSD1306 on the great [tutorial about
the OLED featherwing from Adafruit](https://learn.adafruit.com/adafruit-oled-featherwing/circuitpython#usage-6-4).
