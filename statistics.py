import numpy as np
def calculateStats(numbers):
  if len(numbers)==0:
    return {"avg": float('nan'), "max": float('nan'), "min": float('nan')}
        
  else:
    return {"avg": np.mean(numbers), "max": max(numbers), "min": min(numbers)}
        
