class Solution:
    def convertBinary(self, n):
        binary = ""
        if (n != 0):
            while (n >= 1):
                if (n % 2 == 0):
                    binary = binary + "0"
                    n = n / 2
                else:
                    binary = binary + "1"
                    n = (n-1) / 2

        else:
            binary = "0"

        return "".join(reversed(binary))

    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        d = []
        for num in arr:
            d.append((num, self.convertBinary(num).count('1')))
            
        d = sorted(d, key=lambda x:x[1])
        
        return [x[0] for x in d]
            
            
#         res = OrderedDict(sorted(d.items(), key=lambda x : x[1]))
        
#         return res.keys()
                        
        
        