# SX1509-WiringPi-Python

Translation of the SX1509 driver for WiringPi, with some naming changes

## Prereqs

* WiringPi
* WiringPi-Python

## API

### Constants

* Pin Mode
  * SX1509.PIN_MODE['OUTPUT'], SX1509.PIN_MODE['INPUT'], SX1509.PIN_MODE['PWM']
* Digital values
  * SX1509.PIN_STATE['HIGH'], SX1509.PIN_STATE['LOW']

### Methods

* SX1509(address=0x3E, interruptPin=None, resetPin=None, oscillatorPin=None)
  * Constructor, pass in the I2C address of the SX1509 (defaults to 0x3E), hardware interrupt pin, hardware reset pin, and hardware oscillator pin. Begins I2C comms and checks for SX1509 at address given, throws error if not found
* .reset(hardware=False)
  * Resets the SX1509, using software if hardware is False or if resetPin == None, hardware reset pin otherwise. Throws an error if hardware == True but resetPin == None
* .pinMode(pin, mode)
  * sets pin to mode. Mode should be SX1509.OUTPUT, SX1509.INPUT, SX1509.PWM
* .digitalWrite(pin, value)
  * Writes the digital value to pin, value should be SX1509.HIGH or SX1509.LOW
* .read(pin)
  * digital read of pin, returns SX1509.HIGH or SX1509.LOW
* .PWMWrite(pin, value)
  * PWM write to pin of value, errors if pin mode is not SX1509.PWM


### Utils (not necessairily needed for use, called by API methods)

* .startClock(internal=True)
  * starts the clock oscillations for PWM use
* .pullupResistor(pin, enable=False)
  * sets the pullup resistor value for pin
* .inputBuffer(pin, enable=False)
  * sets the input buffer for pin
