class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            c = [0] * 26
            for ch in s:
                c[ord(ch) - ord('a')] += 1
                
            res[tuple(c)].append(s)
            
        return res.values()