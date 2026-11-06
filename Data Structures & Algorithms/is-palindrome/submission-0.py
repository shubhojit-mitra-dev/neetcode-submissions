class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean: str = "".join([c.lower() for c in s if c.isalnum()])
        return clean[::-1] == clean