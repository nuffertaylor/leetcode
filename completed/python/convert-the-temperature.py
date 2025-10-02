class Solution(object):
    def convertTemperature(self, celsius):
        return [self.convertToK(celsius), self.convertToF(celsius)]
    
    def convertToF(self, celsius):
        return celsius * 1.8 + 32

    def convertToK(self, celsius):
        return celsius + 273.15