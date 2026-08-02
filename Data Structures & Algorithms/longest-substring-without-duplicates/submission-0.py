class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()
        left = 0
        longest_substring = 0

        for right in range(len(s)):
            while s[right] in characters:
                characters.remove(s[left])
                left+=1

            characters.add(s[right])
            current_length = right -left +1

            longest_substring = max(longest_substring, current_length)

            
        return longest_substring