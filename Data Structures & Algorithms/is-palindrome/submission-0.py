class Solution:
    def isPalindrome(self, s: str):
        s_lower = s.lower()
        s_alnum = ""
        for elem in s_lower:
            if elem.isalnum():
                s_alnum += elem
        return s_alnum == s_alnum[::-1]

