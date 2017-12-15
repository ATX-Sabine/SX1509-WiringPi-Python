from distutils.core import setup, Extension

extension_mod = Extension("_SX1509", ["SX1509_wrap.cxx", "SX1509_wrap.c"])

setup(name = "SX1509", ext_modules=[extension_mod])