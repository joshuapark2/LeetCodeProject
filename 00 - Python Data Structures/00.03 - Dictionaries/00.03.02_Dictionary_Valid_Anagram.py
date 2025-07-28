# 32.05.01 - LC - Contains Duplicate
'''
class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    hash1, hash2 = {}, {}

    if len(s) != len(t):
      return False

    for i in range(len(s)):
      hash1[s[i]] = 1 + hash1.get(s[i], 0)
      hash2[t[i]] = 1 + hash2.get(t[i], 0)
    
    return hash1 == hash2
    
# Creating an instance of the class
solution = Solution()
print(solution.isAnagram("racecar", "carrace"))  # Output: True
print(solution.isAnagram("jar", "jam"))  # Output: False
'''

### Create an empty dictionary:
newDict = {}

### give 2 key,value pairs to the dictionary
newDict["hello"] = 1
newDict["bye"] = 2
# print(newDict) -> {'hello': 1, 'bye': 2}

### Increment hello by 1, decrement bye by 1
newDict["hello"] = 1 + newDict.get("hello", 0) #! default value for .get() is important
newDict["bye"] = newDict.get("bye", 0) - 1
# print(newDict) -> {'hello': 2, 'bye': 1}

### Give a Key Error -> A key that doesn't exist
# print(newDict["hello"]) -> 2
#! print (newDict["keyError"]) -> KeyError: 'keyError'

### Give a Type Error -> adding a string to a int should give a Type Error
# newDict["hello"] = 'a' + newDict["hello"]
#! TypeError: can only concatenate str (not "int") to str

newDict["hello"] = 1 + newDict["not_Available"]