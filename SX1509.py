class SX1509:

  REGISTERS = {
    'CHECK': 0x13
  }

  PIN_MODE = {
    'OUTPUT': 0,
    'INPUT': 1,
    'PWM': 3
  }

  PIN_STATE = {
    'LOW': 0,
    'HIGH': 1
  }

  def __init__(self, address=0x3E, interruptPin=None, resetPin=None, oscillatorPin=None):
    self.address = address
    self.interruptPin = interruptPin
    self.resetPin = resetPin
    self.oscillatorPin = oscillatorPin
  