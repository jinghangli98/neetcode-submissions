class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        
        return [num for sublist in [nums] * 2 for num in sublist]