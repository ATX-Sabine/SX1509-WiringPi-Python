%module SX1509
%{
  #include "./SparkFun-SX1509/SparkFunSX1509.h"
  #include "wiringPi.h"
  #include "wiringPiI2C.h"
%}

class SX1509 {
  public:
    SX1509();
    byte begin(byte address, byte resetPin);
    void reset(bool hardware);
    void pinDir(byte pin, byte inOut);
    void writePin(byte pin, byte highLow);
    byte readPin(byte pin);
    void ledDriverInit(byte pin, byte freq, bool log);
    void pwm(byte pin, byte iOn);
    void blink(byte pin, unsigned long tOn, unsigned long tOff, byte onIntensity, byte offIntensity);
    void breathe(byte pin, unsigned long tOn, unsigned long tOff, unsigned long rise, unsigned long fall, byte onInt, byte offInt, bool log);
    void setupBlink(byte pin, byte tOn, byte tOff, byte onIntensity, byte offIntensity, byte tRise, byte tFall, bool log);
    void enableInterrupt(byte pin, byte riseFall);
    unsigned int interruptSource(bool clear);
    void clearInterrupt();
    bool checkInterrupt(int pin);
    void configClock(byte oscSource, byte oscPinFunction, byte oscFreqOut, byte oscDivider);
};