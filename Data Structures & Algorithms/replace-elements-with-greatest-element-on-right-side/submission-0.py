class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for idx, num in enumerate(arr[:-1]):
            arr[idx] = max(arr[idx+1:])
        
        arr[-1] = -1
        return arr