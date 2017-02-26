from distutils.core import setup, Extension
setup(name='extpow10', version='1.0', ext_modules=[Extension('extpow10', ['extpow10.c'])])
