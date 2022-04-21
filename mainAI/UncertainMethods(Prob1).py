import numpy as np
import collections
npArray= np.array([60, 70, 70, 70, 80,90,60])
c=collections.Counter(npArray) # Generate a dictionary {"value":"nbOfOccurrences"}
arraySize=npArray.size
nbOfOccurrences=c[60] #assuming you want the proba to get 10
proba=(nbOfOccurrences/arraySize)*100
print(proba) #print 60.0

# O/P
# 28.57142857142857
