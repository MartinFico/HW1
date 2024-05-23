class IntegerSet:
    def __init__(self, elements=None):
        self.elements = set(elements) if elements else set()

    def add(self, element):
        self.elements.add(element)

    def sum(self):
        return sum(self.elements)

    def mean(self):
        if not self.elements:
            return 0
        return sum(self.elements) / len(self.elements)

    def max(self):
        if not self.elements:
            return None
        return max(self.elements)

    def min(self):
        if not self.elements:
            return None
        return min(self.elements)