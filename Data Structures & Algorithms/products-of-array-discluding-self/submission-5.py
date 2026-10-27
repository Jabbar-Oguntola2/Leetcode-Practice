class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix, postfix = [], []

        running_value = 1
        for num in nums:
            prefix.append(running_value)
            running_value *= num
        
        running_value = 1
        for i in range(len(nums) -1, -1, -1):
            postfix.append(running_value)
            running_value *= nums[i]

        postfix = postfix[::-1]

        for a,b in zip(prefix, postfix):
            res.append(a * b)
        

        return res

        
