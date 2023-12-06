# 380. Insert Delete GetRandom O(1) - Medium

class RandomizedSet:

    def __init__(self):
        self.data_map = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False
        
        self.data_map[val] = len(self.data)
        self.data.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.data_map:
            return False
        
        last_ele_in_list = self.data[-1]
        idx_of_ele_to_remove = self.data_map[val]

        self.data_map[last_ele_in_list] = idx_of_ele_to_remove
        self.data[idx_of_ele_to_remove] = last_ele_in_list

        self.data.pop()
        self.data_map.pop(val)

        return True

    def getRandom(self) -> int:
        import random
        return random.choice(self.data)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()