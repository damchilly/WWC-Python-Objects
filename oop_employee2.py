__author__ = 'dianaamador'
#!/usr/bin/python

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary, age):
      self.name = name
      self.salary = salary
      self.age = age
      Employee.empCount += 1

   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000, 23)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000, 32)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount

emp1.salary = 3000  # Add an 'salary' attribute.
emp2.name = "Lou"  # Modify 'name' attribute.
del emp1.age  # Delete 'age' attribute.
emp1.displayEmployee()
emp2.displayEmployee()