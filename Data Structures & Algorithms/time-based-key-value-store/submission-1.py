class TimeMap:

    def __init__(self):
        self.table = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.table:
            self.table[key] = [[value, timestamp]]
        else:
            self.table[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:

        ans = ""
        values = self.table.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            mid = l + (r-l)//2
            if values[mid][1] == timestamp:
                ans = values[mid][0]
                l = mid + 1
            elif values[mid][1] < timestamp:
                ans = values[mid][0]
                l = mid + 1
            elif values[mid][1] > timestamp:
                r = mid - 1
        
        return ans
        
