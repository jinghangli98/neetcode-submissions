class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        i = 0 #abbr
        j = 0 #word
        while i < len(abbr) and j < len(word):
            if abbr[i].isalpha():
                if abbr[i] != word[j]:
                    return False
                j += 1
                i += 1

            else:
                #if it's number
                if abbr[i] == "0":
                    return False
                
                num = 0
                while i < len(abbr) and abbr[i].isdigit():
                    num = 10 * num + int(abbr[i])
                    i += 1
                
                j += num
        
        return i == len(abbr) and j == len(word)

