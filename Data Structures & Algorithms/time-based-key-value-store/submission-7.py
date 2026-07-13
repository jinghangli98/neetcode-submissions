class TimeMap:

    def __init__(self):
        self.table = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.table:
            self.table[key].append([value, timestamp])
        else:
            self.table[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        if key not in self.table:
            return ans

        values = self.table[key] #(mood, timestamp)
        timestamps = [value[1] for value in values]
        moods = [value[0] for value in values]

        l = 0
        r = len(timestamps) - 1
        while l <= r:
            mid = l + (r-l)//2
            if timestamps[mid] == timestamp:
                return moods[mid]
            elif timestamps[mid] > timestamp:
                r = mid - 1
            elif timestamps[mid] < timestamp:
                ans = moods[mid]
                l = mid + 1
        
        return ans

        
