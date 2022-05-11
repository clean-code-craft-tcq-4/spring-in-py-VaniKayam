
def calculateStats(numbers):
  if len(numbers)==0:
    return float("nan")
        
  else:
    return {"avg": sum(numbers)/len(numbers), "max": max(numbers), "min": min(numbers)}
        
