class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = defaultdict(int)
        count = 0
        for t in time:
            count += d[(60 - t % 60) % 60]
            d[t % 60] += 1
        
        
        return count
        
        
        
        
        
        
        
        
        
        
        
        
        
        # count = 0
        # for i in range(len(time)):
        #     j = i + 1
        #     while j < len(time):
        #         if (time[i] + time[j]) % 60 == 0:
        #             count += 1
        #             j += 1
        #         else:
        #             j += 1
        # return count
            