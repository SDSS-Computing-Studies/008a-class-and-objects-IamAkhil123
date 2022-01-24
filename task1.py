#! python3

<<<<<<< HEAD
=======
snm = "Akhil"
sn = "978721"
g = "11"
list1 = [87,87,87,87,87]
list2 = ["English", "Science", "Math", "PE", "Socials"]
x = 1

classproperty = " "
list1 = " "
list2 = " "

def contructor(snm,sn,g):
 return(snm, sn, g)

def getGrades(list1):
 classproperty = list1

def Courses(list2):
 classproperty = list2

def showGrade(x):
 return list2[x] and list1[x]

def showCourses():
 return list2

def getHonorRoll():
 sm = sum(list1)
 sm1 = sum(list2)
 sm2 = sm/sm1
 if sm2 > 86:
  return True
 else:
  return False

def average():
  sm = sum(list1)
  sm1 = sum(list2)
  sm2 = sm/sm1
  return sm2

a = contructor(snm,sn,g)
print(a)

b = getGrades(list1)
print(b)

c = Courses(list2)
print(c)

d = showGrade(x)
print(d)

showCourses()

getHonorRoll()

average()

>>>>>>> f68db59a687cd1b57c71adf0d6746da1026f6323
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

x = "Akhil"
y = 978721
z = 11
classproperty = []
list = [87,83,89,76,83]
list2 = ["math","english","science","socials","PE"]
g = 2

def contructor(x,y,z):
  return(x,y,z)

con = contructor(x,y,z)
print(con)

def getGrades(list):
  return classproperty.append(list)

def getCourses(list2):
  return classproperty.append(list2)

def showGrade(g):
  return list2[g] and list[g]

show = showGrade(g)
print(show)

def showCourses():
  return list2

showC = showCourses()
print(showC)

def getHonorRoll():
  ns = sum(list)
  nl = len(list2)
  orw = ns/nl
  if orw > 86:
    return True
  else: 
    return False

ghr = getHonorRoll()
print(ghr)

def average():
  ns = sum(list)
  nl = len(list2)
  orw = ns/nl
  return orw

avr = average()
print(avr)


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
<<<<<<< HEAD

=======
>>>>>>> f68db59a687cd1b57c71adf0d6746da1026f6323
main()
"""