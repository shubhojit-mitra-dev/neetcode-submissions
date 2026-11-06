class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        hashmap = {}

        left, right = 0, 0
        while right < len(s):
            if s[right] in hashmap:
                left = max(hashmap[s[right]] + 1, left)
            hashmap[s[right]] = right
            res = max(res, right - left + 1)
            right += 1

        return res
