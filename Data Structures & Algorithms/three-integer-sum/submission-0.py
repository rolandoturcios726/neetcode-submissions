class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = set()
        nums.sort()
        for i in range(len(nums)-2):
            complement = -nums[i]
            result = self.twoSum(complement, nums[i+1:])
            for res in result:
                triplet = (nums[i], res[0], res[1])
                solution.add(triplet)

        return [list(pair) for pair in solution]
        
    def twoSum(self, target, nums):
        seen = set()
        solution = set()

        for num in nums:
            complement = target - num
            if complement in seen:
                solution.add((num,complement))
            seen.add(num)
        
        return [list(pair) for pair in solution]