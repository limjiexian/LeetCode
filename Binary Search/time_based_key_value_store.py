# class TimeMap:

#     def __init__(self):
#         self.storage = {}   # key: list of [val, timestamp]

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         s = self.storage
        
#         if key not in s:
#             s[key] = []
        
#         s[key].append([value, timestamp])
        
#         return

#     def get(self, key: str, timestamp: int) -> str:
#         s = self.storage
#         res = ""

#         arr = s.get(key, [])

#         l, r = 0, len(arr) - 1

#         while l <= r:
#             m = (l + r) // 2

#             # if timestamp == arr[m][1]:
#             #     return arr[m][0]

#             if timestamp < arr[m][1]:   # go left
#                 r = m - 1
#             else:   # here is timestamp >= arr[m][1]
#                 res = arr[m][0]
#                 l = m + 1
            
#         return res



from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)   # key: list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        s = self.storage
        
        # if key not in s:
        #     s[key] = []
        
        s[key].append([value, timestamp])
        
        return

    def get(self, key: str, timestamp: int) -> str:
        s = self.storage
        res = ""

        arr = s.get(key, [])

        l, r = 0, len(arr) - 1

        while l <= r:
            m = (l + r) // 2

            # if timestamp == arr[m][1]:
            #     return arr[m][0]

            if timestamp < arr[m][1]:   # go left
                r = m - 1
            else:   # here is timestamp >= arr[m][1]
                res = arr[m][0]
                l = m + 1
            
        return res
