a=[1,2,3]
b=[x for x in a]
print(b)

name='Anirudh'
name_list=[x for x in name]
print(name_list)

names=['Alex','Barbie','John','Singh','Devoe']
names_list=[x for x in names if len(x)>5]
print(names_list)

import random

student_scores={student:random.randint(1,100) for student in names}
print(student_scores)

passed_students={student:score for (student,score) in student_scores.items() if score >=60}
print(passed_students)