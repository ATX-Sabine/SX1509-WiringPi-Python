import wiringpi

class SX1509:

  REGISTERS = {
    'CHECK': 0x13,
    'RESET': 0x7D,
    'PIN_DIRECTION': 0x0E,
    'PIN_DATA': 0x10,
    'CLOCK': 0x1E,
    'MISC': 0x1F,
    'DISABLE_INPUT_BUFFER': 0x00,
    'PULLUP_RESISTORS': 0x06,
    'LED_DRIVER': 0x20,
    'PWM_INTENSITY': [0x2A, 0x2D, 0x30, 0x33, 0x36, 0x3B, 0x40, 0x45, 0x4A, 0x4D, 0x50, 0x53, 0x56, 0x5B, 0x60, 0x65]
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
    self.i2c = wiringpi.I2C()
    self.device = self.i2c.setup(self.address)
    data = [0x00, 0x00]
    data[0] = self.i2c.readReg8(self.device, self.REGISTERS['CHECK'])
    data[1] = self.i2c.readReg8(self.device, self.REGISTERS['CHECK']+1)
    print(data) 
    
  def reset(self, hardware):
    if hardware:
      if self.resetPin == None:
        raise ValueError('SX1509 cannot hardware reset when .resetPin is None')
      else:
        wiringpi.pinMode(self.resetPin, 1)
        wiringpi.digitalWrite(self.resetPin, 0)
        wiringpi.digitalWrite(self.resetPin, 1)
    else:
      wiringpi.wiringPiI2CWriteReg8(self.address, self.REGISTERS['RESET'], 0x12)
      wiringpi.wiringPiI2CWriteReg8(self.address, self.REGISTERS['RESET'], 0x34)

  