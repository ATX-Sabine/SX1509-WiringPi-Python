all:
	swig -python -c++ -o SX1509_wrap.cc SX1509.i
	g++-7.2.0 -shared -fPIC -I/usr/include/python2.7 -I/usr/include/arm-linux-gnueabihf/python2.7 -I/usr/local/include SparkFun-SX1509/SparkFunSX1509.cpp -o SX1509.o
	g++-7.2.0 -shared -fPIC -I/usr/include/python2.7 -I/usr/include/arm-linux-gnueabihf/python2.7 -I/usr/local/include SX1509_wrap.cc -o SX1509_wrap.o	
	g++-7.2.0 -shared -fPIC -I/usr/include/python2.7 -I/usr/include/arm-linux-gnueabihf/python2.7 -I/usr/local/include SX1509_wrap.o SX1509.o -o _SX1509.so
