# -*- coding: utf-8 -*-

import time

def deprec(func):

  def newFunction(*args, **kwargs):
    print(func.__name__ + " is deprecated")

  return newFunction

