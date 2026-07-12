class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        max_len = 0       

        for v in num_set:
            if v-1 in num_set:
                continue
            
            current = v
            current_len = 1
            while (current +1) in num_set:
                current_len +=1
                current +=1
            
            if current_len > max_len:
                max_len = current_len

        return max_len
            
