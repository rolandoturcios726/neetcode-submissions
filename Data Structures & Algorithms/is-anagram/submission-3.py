class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for i in s:
            if s_dict.get(i) is None:
                s_dict[i] = 1
            else: 
                s_dict[i] = s_dict.get(i) + 1

        for i in t:
            if t_dict.get(i) is None:
                t_dict[i] = 1 
            else: 
                t_dict[i] = t_dict.get(i) + 1

        return s_dict == t_dict
            
