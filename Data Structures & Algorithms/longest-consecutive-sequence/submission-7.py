class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnum = set(nums)
        max_length = 0
        for num in nums:
            if not (num - 1) in setnum:
                length = 1
                while (num + 1) in setnum:
                    length += 1
                    num += 1
                max_length = max(length, max_length)
        
        return max_length
        
        
        
