from data.easy import Easy

""" Class Hard hold 5 list of numbers.
 In project.py, def get_level_difficulty() use thise data."""

class Hard(Easy):
    
    
    def levels(self, level):
        numbers = []
        match level:
            case 1:
                numbers = [2, 2, 3, 3, 4, 5, 6, 7, 8, 9]
            case 2:
                numbers = [2, 3, 3, 4, 4, 5, 6, 7, 8, 9]
            case 3:
                numbers = [2, 3, 4, 4, 5, 6, 7, 8, 9, 9]
            case 4:
                numbers = [3, 4, 5, 6, 6, 7, 7, 8, 8, 9]
            case 5:
                numbers = [4, 6, 6, 7, 7, 8, 8, 9, 9, 9]
            case 6:
                numbers = [4, 6, 6, 7, 7, 8, 8, 9, 9, 9]
        return numbers

