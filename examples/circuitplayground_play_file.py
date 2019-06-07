"""THIS EXAMPLE REQUIRES A WAV FILE FROM THE examples FOLDER IN THE
Adafruit_CircuitPython_CircuitPlayground REPO found at:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples

Copy the "dip.wav" file to your CIRCUITPY drive.

Once the file is copied, this example plays a wav file!"""
from adafruit_circuitplayground.express import cpx

cpx.play_file("dip.wav")
