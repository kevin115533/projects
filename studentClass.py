class Student(object):
    def __init__(self, name, number):
        self._name = name
        self._scores = []
        for count in range(number):
            self._scores.append(0)
            
    def getName(self):
        return self._name
    
    def setScore(self, i, score):
        self._scores[i - 1] = score
        
    def getScore(self, i):
        return self._scores[i - 1]
    
    def getAverage(self):
        return sum(self._scores) / len(self._scores)
    
    def getHighScore(self):
        return max(self._scores)
    
    def __str__(self):
        return "Name: " + self._name + "\nScores: " + " ".join(map(str, self._scores))    
