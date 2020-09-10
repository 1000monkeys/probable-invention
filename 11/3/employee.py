class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def get_raise(self, amount=5000):
        self.salary = int(self.salary) + int(amount)
