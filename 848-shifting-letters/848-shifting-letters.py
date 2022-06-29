class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
               'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']     
        
        res = []
        currSum = sum(shifts)
        idx = 0
        
        for c in s:
            index = char.index(c)
            if idx != 0:
                currSum -= shifts[idx - 1]
                
            index += currSum
            res.append(char[index % 26])
            idx += 1
            
            
        return ''.join(res)
        