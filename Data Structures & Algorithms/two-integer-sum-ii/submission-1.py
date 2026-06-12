class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pa = 0
        pz = len(numbers) - 1
        while pa < pz:
            if numbers[pa] + numbers[pz] == target:
                return [pa+1, pz+1]
            elif numbers[pa] + numbers[pz] > target:
                pz -= 1
            elif numbers[pa] + numbers[pz] < target:
                pa += 1            