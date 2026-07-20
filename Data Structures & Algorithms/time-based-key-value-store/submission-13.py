class TimeMap:

    def __init__(self):
        self.table = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key in self.table:
            self.table[key].append([value, timestamp])
        else:
            self.table[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.table:
            return ""
            
        values = self.table[key]
        ts = [value[1] for value in values]
        moods = [value[0] for value in values]

        l = 0
        r = len(ts) - 1
        ans = ""

        while l <= r:
            mid = (l+r)//2
            if timestamp == ts[mid]:
                
                return moods[mid]

            elif timestamp < ts[mid]:
                r = mid - 1
            
            elif timestamp > ts[mid]:

                ans = moods[mid]
                l = mid + 1

        return ans
        
