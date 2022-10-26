class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        
        right = 0
        writer = 0
        
        while right < n:
            left = right
            while right < n and chars[left] == chars[right]:
                right += 1
            
            chars[writer] = chars[left]
            writer += 1

            count = right - left
            if count > 1:
                for d in str(count):
                    chars[writer] = d
                    writer += 1
        
        return writer