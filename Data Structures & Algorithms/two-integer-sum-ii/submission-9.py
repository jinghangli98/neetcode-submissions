class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers) - 1

        for l in range(len(numbers)):
            
            while numbers[l] + numbers[r] > target:
                r -= 1

            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]

        return ans