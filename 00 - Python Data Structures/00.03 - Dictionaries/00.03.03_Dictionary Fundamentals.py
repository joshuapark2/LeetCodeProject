# Creating dictionary where [] represents key:value pairs (tuples)
tupleDict = dict([(1, 'a'), (2, 'b')])
tupleDict[3] = "squirtle"
tupleDict[1] = "Pikachu"
print(tupleDict)
tupleDictV2 = dict({(1, 'a'), (2, 'b')})
tupleDictV3 = dict({1, 'a'}, {2, 'b'})

# {} - Literal Syntax for an Empty Dictionary (Most Common)
commonDict = {}
commonDict[1] = "Pikachu" # Faster + More readable