class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        l = 0
        window = {}
        ans = float('inf')
        for r in range(len(blocks)):
            if blocks[r] == 'B':
                window['B'] = window.get('B', 0) + 1
            else:
                window['W'] = window.get('W', 0) + 1
            
            while r-l+1 ==k:
                ans = min(ans, window.get('W', 0))
                window[blocks[l]] -= 1
                l += 1
        
        return ans





            


