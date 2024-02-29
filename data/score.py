import math
class Score:


    def __init__(self, difficulty):

        # Saves the values that are multiplied by the current combo when the answer is correct.
        self._difficulty = None      
        match difficulty:
            case "Easy":
                self._difficulty = 1
            case "Medium":
                self._difficulty = 1.2
            case "Hard":
                self._difficulty = 1.4
        
        self._score = 1
        self._time = 0
        self._combo = 1
        self._answer = None


    # Retrieves the value returned by validation_answer.
    def answer(self, value):
        self._answer = value 
        if self._answer == True:
            self.set_combo()
            self.set_score()
        else:
            self._combo = 1      
        

    @property
    def combo(self):
        return self._combo
    
    
    def set_combo(self):
        if self._answer == True:
            self._combo += 5


    @property
    def score(self):
        return f"{self._score}"
    
    
    @property
    def time(self):
        return self._time
    
    
    @time.setter
    def time(self, value):
        self._time += value
     

    def set_score(self):
            #Calculates and updates the current score.
            self._score += math.floor(self._combo * self._difficulty)


    def score_reset(self):
        self._difficulty = None
        self._score = 1
        self._time = 0
        self._combo = 1
        self._answer = None
