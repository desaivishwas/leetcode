class TwoSum:

    def __init__(self):
        self.d = {}

    def add(self, number: int) -> None:
        self.d[number] = 1 + self.d.get(number, 0)

    def find(self, value: int) -> bool:
        
        for num in self.d.keys():
            diff = value - num
            if diff != num:
                if diff in self.d:
                    return True
            elif self.d[num]  > 1:
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)