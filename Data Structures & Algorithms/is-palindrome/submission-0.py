class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = "".join(filter(str.isalnum,s)).lower()
        palindrome = s_clean.lower()[::-1]

        if s_clean.strip().lower() == palindrome:
            return True

        return False

        