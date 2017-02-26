from setuptools import setup

setup(
    name='cffipow10',
    setup_requires=["cffi>=1.0.0"],
    cffi_modules=["cffipow10_builder.py:ffibuilder"],
    install_requires=["cffi>=1.0.0"],
)
