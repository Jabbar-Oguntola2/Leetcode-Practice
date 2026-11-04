class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        left,right = 0, len(heights) - 1
        while left < right:
            width = abs(left - right)
            height = min(heights[left], heights[right])
            area = width * height
            maxarea = max(area, maxarea)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return maxarea
