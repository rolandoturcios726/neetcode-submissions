class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}    
        for i, value in enumerate(nums):
            j = target - value

            if j in seen:
                return list([seen[j],i])
            seen[value] = i
