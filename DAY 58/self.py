class Worker:
    def info(self, name, salary):
        print(f"{name} has to be paid {salary} salary.")

a = Worker()
a.info("John", 5000)  # Output: John has to be paid 500

b = Worker()
b.info("Abhi",10000)  # Output: Abhi has to be paid 10000

# It can also acheived by
class Worker:
    def info(self, name, salary):
        self.name = name
        self.salary = salary
        print(f"{self.name} has to be paid {self.salary} salary.")

a = Worker()
a.info("Abhi", 10000)   # Output: Abhi has to be paid 10000

b = Worker()
b.info("John", 5000)  # Output: John has to be paid 500

# What is self keyword
# self is a reference to the current instance of the class and is used to access variables and methods
