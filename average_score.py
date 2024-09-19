grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students={'Johnny','Bilbo','Steve','Khendrik','Aaron'}
average=[float(sum(grades[0])/len(grades[0])),float(sum(grades[1])/len(grades[1])),float(sum(grades[2])/len(grades[2])),float(sum(grades[3])/len(grades[3])),float(sum(grades[4])/len(grades[4]))]
students_s=list(students)
students_s.sort()
average_score={students_s[0]:average[0],students_s[1]:average[1],students_s[2]:average[2],students_s[3]:average[3],students_s[4]:average[4]}
print(average_score)