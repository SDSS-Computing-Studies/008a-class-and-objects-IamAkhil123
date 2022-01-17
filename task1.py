#! python3

from typing import Match

a = str(input("enter name"))
b = str(input("enter studentnumber"))
c = str(input("enter grade"))
d = str(input("enter class 1"))
e = int(input("enter grade for class"))
f = str(input("enter class 2"))
g = int(input("enter grade for class"))
h = str(input("enter class 3"))
i = int(input("enter grade for class"))
j = str(input("enter class 4"))
k = int(input("enter grade for class"))
l = str(input("enter class 5"))
m = int(input("enter grade for class"))
n = str(input("enter class 6"))
o = int(input("enter grade for class"))
p = str(input("enter class 7"))
q = int(input("enter grade for class"))

while True:
 fv = input("enter a command")

 def average():
  ab = e + g + i + k + m + o + q
  cd = int(ab)/7
  print("Your average grade is",cd)

 if fv == "average":
  average()
 
 def getHonorRoll():
  ab = e + g + i + k + m + o + q
  cd = int(ab)/7
  if cd > 86:
   print("True")
  else:
   print("False")

 if fv == "getHonorRoll":
  getHonorRoll()

 def showCourses():
  print(d, f, h, j, l, n, p)

 if fv == "showCourses":
   showCourses()

 def showGrade():
  if ef == d:
   print(d,e)
  if ef == f:
   print(f,g)
  if ef == h:
   print(h,i)
  if ef == j:
   print(j,k)
  if ef == l:
   print(l,m)
  if ef == n:
   print(n,o)
  if ef == p:
   print(p,q)

 if fv == "showGrade":
   ef = input("Enter the course")
   showGrade()


"""
(10 points) 
Create a class object for a student.
It should have the following properties
str name
str studentNumber
int grade
list courses - to corresepond with course names
list grades - to correspond with grades

It should have the following methods:
average()       - determines the mathematical average of all course grades
getHonorRoll()  - determines the average of the top 5 courses if there are at least 5 courses.
                  returns True if the average is 86 or higher (on the honor roll)
                  returns False if not on the honor roll
showCourses()   - prints a list of all courses
showGrade(int)  - takes 1 parameter, the index of the list
                - displays the course name and grade
getCourses(list)- Receives a list of courses and stores that in the class property
getGrades(list) - Receives a list of grades and stores that in the class property
constructor     - should require the student name, studentNumber and grade (in that order)
"""

class student:

    # properties should be listed first

    def __init__(): # You will need to create your own input parameters for all methods
        pass

    def __del__():
        pass

    def average(self):
        pass

def main():
    # This contains test data that will be used by the autograder.
    # do not modify this function

    st1 = student("Anita Bath","91334",11)
    st1.getCourses( ["English","Math","PE","Computers","History","Biology","Japanese"] )
    st1.getGrades( [91, 94, 87, 99, 82, 100, 73])

    st2 = student("Joe Lunchbox","12346", 11)
    st2.getCourses( ["English","Math","Physics","Computers","Geography","Chemistry","French"] )
    st2.getGrades( [71, 98, 93, 95, 68, 81, 71])




main()