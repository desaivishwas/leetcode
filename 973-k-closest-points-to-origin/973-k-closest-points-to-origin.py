import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y**2)
            minHeap.append([dist,x,y])
            
        heapq.heapify(minHeap)
        print(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append((x,y))
            k -= 1
        return res
            
            
        
        
#             heap = []
#             for x,y in points:
#                 d = -(x*x + y*y)
#                 heapq.heappush(heap, (d,x,y))
#                 if len(heap) > k:
#                     heapq.heappop(heap)

#             ret = []
#             for d,x,y in heap:
#                 ret.append((x,y))

#             return ret

        
        