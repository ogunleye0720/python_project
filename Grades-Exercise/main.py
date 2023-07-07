#Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.

student_scores = {
    "Harry": 81,
    "Ran": 78,
    "Hermiane": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for keys in student_scores:
    scores = student_scores[keys]
    if (scores >= 91 and scores <= 100 ):
        student_grades.update({keys: "Outstanding"})
    elif (scores >= 81 and scores <= 90 ):
        student_grades.update({keys: "Exceeds Expectations"})
    elif (scores >= 71 and scores <= 80):
        student_grades.update({keys: "Acceptable"})
    else:
        student_grades.update({keys: "Fail"})

print(student_grades) 