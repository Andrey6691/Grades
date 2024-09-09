average_score={}
grades=[[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students={'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a=(sum(grades[0])/len(grades[0]))
b=(sum(grades[1])/len(grades[1]))
c=(sum(grades[2])/len(grades[2]))
d=(sum(grades[3])/len(grades[3]))
e=(sum(grades[4])/len(grades[4]))
students_list=list(students)
students_sorted=sorted(students_list)
A=students_sorted[0]
B=students_sorted[1]
C=students_sorted[2]
D=students_sorted[3]
E=students_sorted[4]
average_score.update({A:a, B:b,C:c,D:d,E:e})
print(average_score)