import time
import math
import sys
from random import randint
import colorsys

sys.path.append('../')

from SX1509 import SX1509

expander = SX1509(0x3E)
expander.reset(False)
expander.startInternalClock()
expander.setDisableInputBuffer(5, True)
expander.setDisableInputBuffer(6, True)
expander.setDisableInputBuffer(7, True)
expander.setPullupResistor(5, True)
expander.setPullupResistor(6, True)
expander.setPullupResistor(7, True)
expander.setPinDirection(5, expander.PIN_MODE['OUTPUT'])
expander.setPinDirection(6, expander.PIN_MODE['OUTPUT'])
expander.setPinDirection(7, expander.PIN_MODE['OUTPUT'])
expander.setDigitalPinValue(5, 0)
expander.setDigitalPinValue(6, 0)
expander.setDigitalPinValue(7, 0)
expander.startInternalClock()
expander.enableLEDDriver(5, True)
expander.enableLEDDriver(6, True)
expander.enableLEDDriver(7, True)

hue = 0

def hsv2rgb(h, s, v):
  h = float(h)
  s = float(s)
  v = float(v)
  h60 = h / 60.0
  h60f = math.floor(h60)
  hi = int(h60f) % 6
  f = h60 - h60f
  p = v * (1 - s)
  q = v * (1 - f * s)
  t = v * (1 - (1 - f) * s)
  r, g, b = 0, 0, 0
  if hi == 0: r, g, b = v, t, p
  elif hi == 1: r, g, b = q, v, p
  elif hi == 2: r, g, b = p, v, t
  elif hi == 3: r, g, b = p, q, v
  elif hi == 4: r, g, b = t, p, v
  elif hi == 5: r, g, b = v, p, q
  r, g, b = int(r * 255), int(g * 255), int(b * 255)
  return r, g, b

while True:
  color = hsv2rgb(hue, 1, 1)
  print(color)
  expander.setPWMPinValue(5, color[0])
  expander.setPWMPinValue(6, color[1])
  expander.setPWMPinValue(7, color[2])
  hue += 3
  if hue > 360:
    hue = 0
  time.sleep(.1)

