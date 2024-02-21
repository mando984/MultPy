from data.easy import Easy

class Medium(Easy):
    def levels(self, level):
         numbers = []
         match level:
            case 1:
                numbers = [2, 2, 2, 3, 3, 4, 4, 5, 5, 5]
            case 2:
                numbers = [2, 2, 3, 3, 3, 4, 4, 4, 5, 5]
            case 3:
                numbers = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
            case 4:
                numbers = [3, 3, 3, 4, 4, 4, 5, 6, 6, 6]
            case 5:
                numbers = [3, 3, 3, 4, 4, 4, 6, 6, 6, 6]
            case 6:
                numbers = [3, 3, 3, 4, 4, 4, 6, 6, 6, 6]

         return numbers
    
   