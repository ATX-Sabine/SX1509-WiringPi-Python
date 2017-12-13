%module SX1509
%{
  #include "./SparkFun-SX1509/SparkFunSX1509.h"
%}

class SX1509 {
  SX1509();
  byte begin(byte address, byte resetPin);
  void reset(bool hardware);
};