# 32.05.01 - LC - Contains Duplicate
from typing import List

class Solution:
    def hasDuplicate_hashSet(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
    def hasDuplicate_Brute_Force(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    
    def hasDuplicate_Sorting(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
    
    def hasDuplicate_Hash_Set_Length(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)


# Creating an instance of the class
solution = Solution()
print(solution.hasDuplicate_hashSetLength([1, 2, 3, 4]))  # Output: False
print(solution.hasDuplicate_hashSetLength([1, 2, 3, 1]))  # Output: True