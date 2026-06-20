class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sol = {}
        for i, value in enumerate(nums):
            if value not in sol:
                sol[value] = 0
            sol[value] +=1

        return sorted(sol, key = sol.get, reverse = True)[:k]
        
