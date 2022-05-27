class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i, out = 0, []
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            out.append(intervals[i])
            i += 1
            
        # merging overlapping intervals
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        out.append(newInterval)

        
        while i < len(intervals):
            out.append(intervals[i])
            i += 1
            
        
        return out
            
        
        
        