class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for sub_str in strs:
            res += str(len(sub_str)) + "#" + sub_str
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            num = int(s[i:j])
            word = s[j+1:num+j+1]
            res.append(word)

            i = j + 1 + num

        return res



            

