
''' 1 '''

class Student:
    def __init__(self, name, math, literature, english):
        self.name = name
        self.msc = math
        self.lsc = literature
        self.esc = english
    
    def score(self):
        score = round((self.msc+self.lsc+self.esc)/3, 2)
        print('\nThe average mark of', self.name, 'is', score)

obt = Student(input("name: "),
                float(input("math'score: ")), 
                float(input("literture's score: ")), 
                float(input("english's score: ")))
obt.score()