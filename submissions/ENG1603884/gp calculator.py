''''This code calculates the cgpa of students'''

print('Enter the total number of courses you offer:')
course_number = int(input())

# creates empty lists to store the inputs from the users
courses = []
grade_points = []
credit_points = []
sub_totalList = []


for a in range(course_number):#a loop that loops according to the number of courses offered


    def convertGrade(grade):#function that converts the grade of the student to grade points
        if grade == 'A' or grade == 'a':
            return 5
        elif grade == 'B' or grade == 'b':
            return 4
        elif grade == 'C' or grade == 'c':
            return 3
        elif grade == 'D' or grade == 'd':
            return 2
        elif grade == 'F' or grade == 'f':
            return 0

    print('Enter the course code:')
    course = input()
    courses.append(course)#adds the input to the course list
    print('Enter the course credit:')
    credit = int(input())
    credit_points.append(credit)#adds input to the credit_points list
    print('Enter your grade for the course:')
    grade = input()
    convertGrade(grade)#the function to convert the grades is called
    sub_total = convertGrade(grade)*credit
    sub_totalList.append(sub_total)#adds input to the sub_totalList list
    grade_points.append(grade)#adds input to the grade_points list


gpa = sum(sub_totalList)/sum(credit_points)#gpa formula
print("Your GP is " + gpa)
