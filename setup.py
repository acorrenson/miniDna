# -*- coding: utf-8 -*-

from setuptools import setup
import src.miniDna as md

setup(
  name='miniDna',
  version=md.__version__,
  license='MIT',
  description='Python module to discover bioinformatic',
  author='Arthur Correnson',
  author_email='arthur.correnson@gmail.com',
  url='https://jdrprod.github.io/miniDna',
  packages=['src/miniDna'],
  )
