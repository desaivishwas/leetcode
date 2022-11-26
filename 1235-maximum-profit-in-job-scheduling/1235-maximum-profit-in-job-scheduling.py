class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)
        arr = list(zip(startTime, endTime, profit))
        arr = sorted(arr, key=lambda x: x[1])
        
        d = defaultdict(lambda: 0)
        
        def binary_search(target, lt):
            low, high, ans = 0, lt, 0
            
            while(high>=low):
                mid = low + (high-low)//2
                t = arr[mid][1]
                if(t>target):
                    high = mid - 1
                else:
                    low = mid + 1
                    ans = d[t]
                
            return ans
        
        ans = 0
        for i in range(n):
            s,e,p = arr[i]
            d[e] = max(ans, p+binary_search(s, i-1))
            ans = d[e] 
            
        return ans
        