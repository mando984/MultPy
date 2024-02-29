""" Class Easy hold 5 list of numbers.
 In project.py, def get_level_difficulty() use thise data."""

class Easy():


    def __init__(self, level = 1):
        self._level = level
        self.numbers = self.levels(self._level)


    @property
    def get_level(self):
        return self.numbers
    
    
    def levels(self, level):
        numbers = []
        match level:
            case 1:
                numbers = [1, 1, 1, 2, 2, 2, 2, 10, 10, 10]
            case 2:
                numbers = [1, 1, 2, 2, 2, 2, 5, 5, 10, 10]
            case 3:
                numbers = [2, 2, 2, 2, 5, 5, 5, 10, 10 ,10]
            case 4:
                numbers = [2, 2, 2, 2, 5, 5, 5, 5, 5, 10]
            case 5:
                numbers = [2, 2, 2, 2, 5, 5, 5, 5, 5, 5]
            case 6:
                numbers = [2, 2, 2, 2, 5, 5, 5, 5, 5, 5]    

        return numbers
    


