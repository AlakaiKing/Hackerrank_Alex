class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self,firstName,lastName,idNumber,score):
        super().__init__(firstName,lastName,idNumber)
        self.score = score

    def calculate(self):
        a = sum(self.score)/len(self.score)
        if a < 40:
            return "T"
        elif (40 <= a) and (a < 55):
            return "D"
        elif (55 <= a) and (a < 70):
            return "P"
        elif (70 <= a) and (a < 80):
            return "A"
        elif (80 <= a) and (a < 90):
            return "E"
        elif (90 <= a) and (a <= 100):
            return "O"
        else:
            return ""

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
