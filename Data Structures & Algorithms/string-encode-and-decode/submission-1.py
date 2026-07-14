class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for substr in strs:
            res += str(len(substr)) + "#" + substr

        return res

    def decode(self, s: str) -> List[str]:

        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            #j is at the #
            num = int(s[i:j])
            word = s[j+1:j+1+num]
            res.append(word)

            i = j + num + 1
        
        return res
