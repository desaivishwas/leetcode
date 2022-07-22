class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ret = deque([intervals[0]])
        curr_interval = intervals[0]
        
        for next_interval in intervals:
            if curr_interval[1] >= next_interval[0]:
                curr_interval[1] = max(curr_interval[1], next_interval[1])
                ret.pop()
                ret.append(curr_interval)
            else:
                curr_interval = next_interval
                ret.append(curr_interval)
        
        return ret