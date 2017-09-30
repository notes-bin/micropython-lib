import sys
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system's.
sys.path.pop(0)
from setuptools import setup
sys.path.append("..")
import optimize_upip

setup(name='micropython-upip',
      version='1.2.2',
      description='Simple package manager for MicroPython.',
      long_description='Simple self-hosted package manager for MicroPython (requires usocket, ussl, uzlib, uctypes builtin modules). Compatible only with packages without custom setup.py code.',
      url='https://github.com/micropython/micropython-lib',
      author='Paul Sokolovsky',
      author_email='micro-python@googlegroups.com',
      maintainer='MicroPython Developers',
      maintainer_email='micro-python@googlegroups.com',
      license='MIT',
      cmdclass={'optimize_upip': optimize_upip.OptimizeUpip},
      py_modules=['upip', 'upip_utarfile'])
