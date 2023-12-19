'''
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
'''
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        values = self.map[key]
        
        def binarySearch():
            l, r = 0, len(values) - 1
            ans = -1
            while l <= r:
                mid = (l + r) // 2
                if values[mid][1] <= timestamp:
                    ans = l
                    l = mid + 1
                else:
                    r = mid - 1
            return ans 
        index = binarySearch()
        return values[index][0] if index != -1 else ""  

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)