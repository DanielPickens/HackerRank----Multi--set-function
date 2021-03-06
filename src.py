class Multiset:
    def __init__(self):
        self.items = []

    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        return self.items.append(val)

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        if val in self.items:
            return self.items.remove(val)

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        return val in self.items

    def __len__(self):
        # returns the number of elements in the multiset
        return len(self.items)
if __name__ == '__main__':
