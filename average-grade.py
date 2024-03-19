def calculate_average_grade(grades):
    if len(grades) == 0:
        print("Error: the list of grades is empty")
    else:
        print(sum(grades)/len(grades))
calculate_average_grade
grades = [76,34,87,98,23]
average = calculate_average_grade(grades)
print()
#find the average grade 

highest_grade = max(grades)
lowest_grade = min (grades)
print(highest_grade, lowest_grade)
#Lowest grade and Highest Grade

def grade_to_letter(grade):
    if grade >= 90:
        print('A')
    elif grade >= 80:
        print('B')
    elif grade >= 70:
        print('C')
    elif grade >= 60:
        print("D")
    else:
        print('F')
        
letter_grades = [grade_to_letter(grade) for grade in grades]
print()