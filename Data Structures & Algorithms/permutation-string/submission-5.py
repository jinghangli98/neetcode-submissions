class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        def count(array):

            count_array = {}
            for l in array:
                if l in count_array:
                    count_array[l] += 1
                else:
                    count_array[l] = 1
            
            return count_array
            
        count_s1 = count(s1)
        for idx in range(len(s2)-len(s1)+1):
            sub_s2 = s2[idx:idx+len(s1)]
            count_s2 = count(sub_s2)

            if sorted(count_s1.items()) == sorted(count_s2.items()):
                return True
        
        return False