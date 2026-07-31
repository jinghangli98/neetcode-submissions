class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for sub_str in strs:
            ans+= str(len(sub_str)) + "#" + sub_str
        
        return ans


    def decode(self, s: str) -> List[str]:
        l = 0
        ans = []
        while l < len(s):
            r = l
            while s[r] != "#":
                r += 1

            num = int(s[l:r])
            word = s[r+1:r+1+num]
            ans.append(word)
            l = r + num + 1
        
        return ans
