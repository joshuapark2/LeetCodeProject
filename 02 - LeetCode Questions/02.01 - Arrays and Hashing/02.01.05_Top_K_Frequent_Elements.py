class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # hashmap
        freq = [[] for i in range(len(nums) + 1)] # iterate empty array for i times input array + 1

        for n in nums: # Iterate input array
            count[n] = 1 + count.get(n, 0) # hashmap key = index, value = count
        for n, c in count.items(): # get our key/value input/count pairs
                freq[c].append(n) # at count, append the number for our empty list

        res = []
        for i in range(len(freq) - 1, 0, -1): # Start from Top of Count to Bottom
            for n in freq[i]: # looking at just the number
                res.append(n) # how we're getting our answer
                if len(res) == k: # res starts at 0 and gets bigger as we append
                    return res