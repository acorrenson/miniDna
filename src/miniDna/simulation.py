# -*- coding: utf-8 -*-

def identityProbability(gs: int, mr: float = 1e-08) -> float:
  """Return the probabilty for a sequence 
    to not change over n generations of evolution.
    
    **Keyword arguments:**  
    gs -- number of generations  
    mr -- mutation rate (default is 1e-08)  
  """

  return math.pow(1-mr, gs)