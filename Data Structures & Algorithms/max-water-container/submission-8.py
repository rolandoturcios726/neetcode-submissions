class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_size = 0
        while left < right:
      
            current_size = min(heights[left], heights[right]) * (right - left)

            if current_size > max_size:
                max_size = current_size
            if heights[left] < heights[right]:
                left +=1
               
            else:
                right -=1
            
     
        return max_size
