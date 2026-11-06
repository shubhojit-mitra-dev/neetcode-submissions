class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["Hello", "World"] -> 5#Hello5#World
        res: str = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # 5#Hello5#World -> 
        res: List[str] = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1 : j+length+1])
            i = j + length + 1
        return res
