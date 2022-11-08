class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        d = set()
        
        for word in words:
            m = ""
            for char in word:
                m += morse[ord(char) - ord('a')]
            print(m)
            d.add(m)
        return len(d)