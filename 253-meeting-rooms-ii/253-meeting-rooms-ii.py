class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # print(intervals[1][0])
        start = sorted([start for start, end in intervals])
        end =  sorted([end for start,end in intervals])
        
        res, count = 0, 0 
        s, e= 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
                
            res = max(res, count)
            
        return res
        