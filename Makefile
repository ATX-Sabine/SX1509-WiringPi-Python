all:
	swig -python -c++ -o SX1509_wrap.cc SX1509.i
	python setup.py build_ext --inplace