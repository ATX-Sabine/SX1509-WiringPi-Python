import time
import sys
sys.path.append('../')

from SX1509 import SX1509

expander = SX1509(0x3E)

expander.reset(False)
expander.enablePWMPins([5, 6, 7])

expander.setPWMPinValue(5, 0xFF)
expander.setPWMPinValue(6, 0x00)
expander.setPWMPinValue(7, 0xFF)
