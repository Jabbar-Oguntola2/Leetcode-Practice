class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        running_value = 1
        for num in nums:
            res.append(running_value)
            running_value *= num
        
        running_value = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= running_value
            running_value *= nums[i]

        return res

        
