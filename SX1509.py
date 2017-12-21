import wiringpi

class SX1509:

  REGISTERS = {
    'CHECK': 0x13,
    'RESET': 0x7D
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
    wiringpi.wiringPiSetupSys()
    wiringpi.wiringPiI2CSetup(self.address)
    data = wiringPiI2C(self.REGISTERS['CHECK'])
    print(data)

  def reset(bool hardware):
    if hardware:
      if self.resetPin == None:
        raise PinError('SX1509 cannot hardware reset when .resetPin is None')
      else:
        wiringpi.pinMode(self.resetPin, 1)
        wiringpi.digitalWrite(self.resetPin, 0)
        wiringpi.digitalWrite(self.resetPin, 1)
    else:
      wiringpi.wiringPiI2CWriteReg8(self.REGISTERS['RESET'], 0x12)
      wiringpi.wiringPiI2CWriteReg8(self.REGISTERS['RESET'], 0x34)

  