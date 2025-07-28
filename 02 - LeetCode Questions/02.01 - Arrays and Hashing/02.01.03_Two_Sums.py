# 32.05.01 - LC - Contains Duplicate
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # val : index

        for index, number in enumerate(nums):
            difference = target - number
            if difference in hashmap:
                return [hashmap[difference], index]
            hashmap[number] = index
    
    def twoSum_bruteForce(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    
    def twoSum_hashMapTesting(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in hashmap:
                return [hashmap[value], index]
            hashmap[index] = value

        


# Creating an instance of the class
solution = Solution()
print(solution.twoSum_hashMapTesting([3, 4, 5, 6], 7)) # Output: [0, 1]
print(solution.twoSum_hashMapTesting([4, 5, 6], 10)) # Output: [0, 2]
print(solution.twoSum_hashMapTesting([5, 5], 10)) # Output: [0, 1]