class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d = defaultdict(int)
        res = 0
        
        for word in words:
            rev = word[1] + word[0]
            if d[rev] > 0:
                res += 4
                d[rev] -= 1
            else:
                d[word] += 1
                
        for word in d:
            if word[0] == word[1] and d[word] > 0:
                res += 2
                break
                
        return res
                