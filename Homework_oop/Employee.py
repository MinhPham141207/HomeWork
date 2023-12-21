''' 2 '''

class Employee:
    def __init__(self, name, worktime, salary, coefficient):
        self.name = name
        self.wt = worktime
        self.slr = salary
        self.cefc = coefficient

    def salary(self):
        salary = self.wt*self.slr*self.cefc - 10**6
        if salary > 9*10**6:
            salary *= 0.9
        print('The amount of salary of', self.name, 'is', salary)

obj = Employee(input("name: "), 
               float(input("worktime (month): ")), 
               float(input("salary per month: ")), 
               float(input("coefficient: ")))

obj.salary()