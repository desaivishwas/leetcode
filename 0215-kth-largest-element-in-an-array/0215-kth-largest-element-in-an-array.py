class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapify(heap)
        for i in range(len(nums)):
            if len(heap) <= k or nums[i] > heap[0]:
                heappush(heap, nums[i])
                if len(heap) > k:
                    heappop(heap)
                    
        return heap[0]
    