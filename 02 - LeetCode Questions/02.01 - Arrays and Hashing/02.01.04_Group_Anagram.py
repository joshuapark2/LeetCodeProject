# 32.05.04 - LC - Group Anagram
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)  # Maps sorted word -> list of anagrams
        
        for word in strs:
            sorted_word = ''.join(sorted(word))  # Sort letters and use as key
            anagram_map[sorted_word].append(word)  # Add original word to the key
        
        return (anagram_map.values())  # Return grouped anagrams

# Creating an instance of the class
solution = Solution()
print(solution.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))

#print(sorted('joshua')) #.join() can only be used on objects like List
#print(''.join(['a', 'h', 'j', 'o', 's', 'u']))

'''
! Version 2
'''

# How do we take the letters of a word, scan the rest of our list 
# and group them together?

print(sorted('eat'))

strs = ["eat"]

anagram_map = {}

for word in strs:
    key = ''.join(sorted(word))
    anagram_map[key] = anagram_map.get(key, []) + [word]
print(list(anagram_map.values()))