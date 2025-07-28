# 32.05.01 - LC - Contains Duplicate

class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    hashmap_S, hashmap_T = {}, {}

    for index in range(len(s)):
      hashmap_S[s[index]] = 1 + hashmap_S.get(s[index], 0)
      hashmap_T[t[index]] = 1 + hashmap_T.get(t[index], 0)
    return hashmap_S == hashmap_T
  
  def isAnagram_Optimized(self, s: str, t: str) -> bool:
      if len(s) != len(t):
        return False
      count = [0] * 26
      for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
      for value in count:
        if value != 0:
          return False
      return True
        



  # 32.04.07 - Python Sorting Techniques Deeper Dive
  def isAnagram_Sorting(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    print(sorted(s))
    print(sorted(t))
    return sorted(s) == sorted(t)
  
  def isAnagram_Hash_Table(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False
    
    countS, countT = {}, {}
    for i in range(len(s)):
      countS[s[i]] = 1 + countS.get(s[i], 0)
      countT[t[i]] = 1 + countT.get(t[i], 0)

    return countS == countT
    
# Creating an instance of the class
solution = Solution()
print(solution.isAnagram_Hash_Table("racecar", "carrace"))  # Output: True
print(solution.isAnagram_Hash_Table("jar", "jam"))  # Output: False