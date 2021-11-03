class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = ''.join(sorted(s1))
        curr = ''
        for char in s2:
            curr += char
            if len(curr) == len(target):
                
                if ''.join(sorted(curr)) == target:
                    return True
                curr = curr[1:]
        return False