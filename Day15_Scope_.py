class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
        
    def computeDifference(self):
        max_element = max(self.__elements)
        min_element = min(self.__elements)
        max_difference = max_element - min_element
        self.maximumDifference = max_difference
