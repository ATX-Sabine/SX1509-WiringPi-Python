import time
import sys
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

expander.setPWMPinValue(5, 0xFF)
expander.setPWMPinValue(6, 0x00)
expander.setPWMPinValue(7, 0xFF)
