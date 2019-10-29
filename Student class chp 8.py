#Anthony Barrante
#ITP 100
#Chapter 8 Project
#This program compares two student objects

StudentName =[('John', 'Smith'), ('Jane', 'Doe'),
              ('Jimmy', 'Neutron'), ('Agent', 'Smith')]

class Student(object):
    #represents a student

    def __init__(self, Fname, Lname):
        #creates a student with First and Names
        self.f = Fname
        self.l = Lname

    def _eq_(self, other):
        #Tests for Equality (Underscores for Priority)
        return self.Fname == other.Fname and self.Lname == other.Lname

    def _ne_(self, other):
        #Tests for inequality (2nd in Priority)
        return self.Fname != other.Fname and self.Lname == other.Lname

    def keyfunction(item):
        #Compares the Last Names of the students by assigning a key
        return item
        

    def __str__(self):
        #Returns string of student objects
        return ("Name: " + self.f + self.l )

    sorted(StudentName, key=keyfunction)

import random

StudentName =[('John', 'Smith'), ('Jane', 'Doe'),
              ('Jimmy', 'Neutron'), ('Agent', 'Smith')]
random.shuffle(StudentName)

print(StudentName)

    
    
