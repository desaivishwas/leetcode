class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0
        i = 0

        while i < len(chars):
            j = chars[i]
            count = 0
            while i < len(chars) and chars[i] == j:
                count+=1
                i+=1
            chars[index] = j
            index += 1
            if count > 1:
                count = str(count)
                for c in count:
                    chars[index] = c
                    index += 1
        return index