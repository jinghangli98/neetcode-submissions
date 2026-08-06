class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        lut = {c:idx for idx, c in enumerate(order)}

        for i in range(len(words)-1):
            word = words[i]
            nxt_word = words[i+1]
            
            min_length = min(len(word), len(nxt_word))
            for ii in range(min_length):
                letter_1 = word[ii]
                letter_2 = nxt_word[ii]
                
                if letter_1 != letter_2:

                    if lut[letter_2] < lut[letter_1]:
                        return False
                    
                    break
            else:
                if len(word) > len(nxt_word):
                    return False
    
        return True
