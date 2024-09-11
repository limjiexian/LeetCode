class TimeMap:

    def __init__(self):
        self.store = {} # key: [value, timestamp]

    # store key with the value at the given timestamp
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])

        # binary search
        l, r = 0, len(values)-1
        
        res = ""
        while l <= r:
            mid = (l+r) // 2

            if values[mid][1] == timestamp:
                return values[mid][0]

            if values[mid][1] < timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return res

    
    # create a time based key value data structure
    # for a same key, 
    # to store multiple values for it at specified time stamps
    # to retrieve the key's value at specified time stamps

