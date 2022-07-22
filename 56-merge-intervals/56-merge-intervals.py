class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        p1, p2 = 0, 1
        while p1 < len(intervals) - 1:
            if intervals[p1][1] >= intervals[p2][0]:
                if intervals [p1][1] < intervals[p2][1]:
                    intervals[p1][1] = intervals[p2][1]
                intervals.remove(intervals[p2])
            else:
                p1 += 1
                p2 += 1
        return intervals 
        