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
    if data[0] != 0xFF or data[1] != 0x00:
      raise Error('SX1509 not detected!')
    self.reset(False)

  def reset(self, hardware):
    if hardware:
      if self.resetPin == None:
        raise ValueError('SX1509 cannot hardware reset when .resetPin is None')
      else:
        wiringpi.pinMode(self.resetPin, 1)
        wiringpi.digitalWrite(self.resetPin, 0)
        wiringpi.digitalWrite(self.resetPin, 1)
    else:
      self.i2c.writeReg8(self.device, self.REGISTERS['RESET'], 0x12)
      self.i2c.writeReg8(self.device, self.REGISTERS['RESET'], 0x34)

  def startInternalClock(self): 
    clockStatus = self.i2c.readReg8(self.device, self.REGISTERS['CLOCK'])
    clockStatus = [0x00, clockStatus]
    miscStatus = self.i2c.readReg8(self.device, self.REGISTERS['MISC'])
    miscStatus = [0x00, miscStatus]
    clockStatus = self.useBitMask(clockStatus, 5, False)
    clockStatus = self.useBitMask(clockStatus, 6, True)
    miscStatus = self.useBitMask(miscStatus, 6, False)
    miscStatus = self.useBitMask(miscStatus, 5, False)
    miscStatus = self.useBitMask(miscStatus, 4, True)
    print(clockStatus)
    print(miscStatus)
    self.i2c.writeReg8(self.device, self.REGISTERS['MISC'], miscStatus[1])
    self.i2c.writeReg8(self.device, self.REGISTERS['CLOCK'], clockStatus[1])

  def setDisableInputBuffer(self, pin, disableInputBuffer):
    disableInputBufferStatus = [0x00, 0x00]
    disableInputBufferStatus[0] = self.i2c.readReg8(self.device, self.REGISTERS['DISABLE_INPUT_BUFFER'])
    disableInputBufferStatus[1] = self.i2c.readReg8(self.device, self.REGISTERS['DISABLE_INPUT_BUFFER'] + 1)
    disableInputBufferStatus = self.useBitMask(disableInputBufferStatus, pin, disableInputBuffer)
    self.i2c.writeReg8(self.device, self.REGISTERS['DISABLE_INPUT_BUFFER'], disableInputBufferStatus[0])
    self.i2c.writeReg8(self.device, self.REGISTERS['DISABLE_INPUT_BUFFER'] + 1, disableInputBufferStatus[1])

  def setPullupResistor(self, pin, pullupResistorOn):
    pullupResistorStatus = [0x00, 0x00]
    pullupResistorStatus[0] = self.i2c.readReg8(self.device, self.REGISTERS['PULLUP_RESISTORS'])
    pullupResistorStatus[1] = self.i2c.readReg8(self.device, self.REGISTERS['PULLUP_RESISTORS'] + 1)
    pullupResistorStatus = self.useBitMask(pullupResistorStatus, pin, pullupResistorOn)
    self.i2c.writeReg8(self.device, self.REGISTERS['PULLUP_RESISTORS'], pullupResistorStatus[0])
    self.i2c.writeReg8(self.device, self.REGISTERS['PULLUP_RESISTORS'] + 1, pullupResistorStatus[1])

  def setPinDirection(self, pin, direction):
    currentPinState = [0x00, 0x00]
    currentPinState[0] = self.i2c.readReg8(self.device, self.REGISTERS['PIN_DIRECTION'])
    currentPinState[1] = self.i2c.readReg8(self.device, self.REGISTERS['PIN_DIRECTION'] + 1)
    bitOn = True
    if direction == 'output':
      bitOn = False
    newPinState = self.useBitMask(currentPinState, pin, bitOn)
    self.i2c.writeReg8(self.device, self.REGISTERS['PIN_DIRECTION'], newPinState[0])
    self.i2c.writeReg8(self.device, self.REGISTERS['PIN_DIRECTION'] + 1, newPinState[1])

  def setDigitalPinValue(self, pin, value):
    currentPinState = [0x00, 0x00]
    currentPinState[0] = self.i2c.readReg8(self.device, self.REGISTERS['PIN_DATA'])
    currentPinState[1] = self.i2c.readReg8(self.device, self.REGISTERS['PIN_DATA'] + 1)
    bitOn = True
    if not bitOn == 1:
      bitOn = False
    newPinState = self.useBitMask(currentPinState, pin, bitOn)
    self.i2c.writeReg8(self.device, self.REGISTERS['PIN_DATA'], newPinState[0])
    self.i2c.writeReg8(self.device, self.REGISTERS['PIN_DATA'] + 1, newPinState[1])

  def enableLEDDriver(self, pin, LEDDriverOn):
    ledDriverState = [0x00, 0x00]
    ledDriverState[0] = self.i2c.readReg8(self.device, self.REGISTERS['LED_DRIVER'])
    ledDriverState[1] = self.i2c.readReg8(self.device, self.REGISTERS['LED_DRIVER'] + 1)
    ledDriverState = self.useBitMask(ledDriverState, pin, LEDDriverOn)
    self.i2c.writeReg8(self.device, self.REGISTERS['LED_DRIVER'], ledDriverState[0])
    self.i2c.writeReg8(self.device, self.REGISTERS['LED_DRIVER'] + 1, ledDriverState[1])

  def enablePWMPin(self, pin):
    self.startInternalClock()
    self.disableInputBuffer(pin, True)
    self.setPullupResistor(pin, True)
    self.setPullupResistor(pin, 'output')
    self.setDigitalPinValue(pin, 0)
    self.startInternalClock()
    self.enableLEDDriver(pin, True)

  def setPWMPinValue(self, pin, value):
    # byteValue = 0xFF & value
    self.i2c.writeReg8(self.device, self.REGISTERS['PWM_INTENSITY'][pin - 1], value)

  def useBitMask(self, currentState, bit, bitOn):
    mask = [0x00, 0x00]
    maskBase = 0x0000
    maskBase |= (1 << bit)
    if not bitOn:
      maskBase = ~maskBase
    highByte = maskBase >> 8
    if bitOn:
      mask[0] = currentState[0] | highByte
      mask[1] = currentState[1] | maskBase
    else:
      mask[0] = currentState[0] & highByte
      mask[1] = currentState[1] & maskBase
    return mask



