# 32.06.7 - Difference between HashMap, Hash Set, Set, and Dictionaries

#! Sets
###   Creating set   ###
hashset = {1, 2, 3, 4, 5}
print("Hash Set: ", hashset)
print(2 in hashset)  # Output: True

hashSetSingle = {1}
print('single element: ',type(hashSetSingle))
hashSetConstructor = set([1, 2, 3, 4, 5])
print("Hash Set Constructor: ", hashSetConstructor)

###   Creating Empty set   ###
emptySet = set()
print(type(emptySet))

###   Adding to Populated set  ###
emptySet.add(1) # How to Add Set
print("empty set: ", emptySet, " type: ", type(emptySet))

print()

#! Dictionary
### Creating Dictionary
dictionary = {'a': 1}
print(dictionary["a"]) # Output: 1

###   Empty Dictionary   ###
emptyDict = {}
print(type(emptyDict))

###   Adding to Empty Dictionary   ###
emptyDict["a"] = 1 # How to Add Dictionaries (key:value pairs)
emptyDict["b"] = 2
print("empty dict: ", emptyDict, " type: ", type(emptyDict))
# empty_dict.add(1) -> dictionaries don't have add method
# AttributeError: 'dict' object has no attribute 'add'

###   Adding to Populated Dictionary   ###
populatedDict = {'a': 1, 'b': 2}
print("populated dict: ", populatedDict, " type: ", type(populatedDict))