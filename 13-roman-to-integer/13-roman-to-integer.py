class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
        res = values.get(s[-1])
        for i in reversed(range(len(s) - 1)):
            if values[s[i]] < values[s[i+1]]:
                res -= values[s[i]]
            else:
                res += values[s[i]]
                
        return res
