class Solution:
    def frequencySort(self, s: str) -> str:
        heap = []
        # d = collections.Counter(s)
        d = {}
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        
        for char, freq in d.items():
            heapq.heappush(heap,(-freq,char))
        res = []
        while heap:
            freq, char = heapq.heappop(heap)
            res.append(-freq*char)
        return ''.join(res)
        