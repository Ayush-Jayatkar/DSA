# Sparse matrix 
sparse_matrix = {
    (1, 0): 85,   
    (2, 3): 92    
    }

num_students = 4
num_subjects = 4


subject_totals = [0] * num_subjects
subject_counts = [0] * num_subjects
student_grades = [0] * num_students

for (student, subject), grade in sparse_matrix.items():
    subject_totals[subject] += grade
    subject_counts[subject] += 1
    student_grades[student] = max(student_grades[student], grade)

subject_averages = [total / count if count > 0 else 0 for total, count in zip(subject_totals, subject_counts)]

students_with_highest_grades = [grade for grade in student_grades]

max_average = max(subject_averages)
subject_with_max_average = subject_averages.index(max_average)

print("Average grade for each subject:")
for i, avg in enumerate(subject_averages):
    print(f"Subject {i}: {avg:.2f}")

print("\nHighest grade for each student:")
for i, grade in enumerate(students_with_highest_grades):
    print(f"Student {i}: {grade}")

print("\nSubject with the highest average grade:")
print(f"Subject {subject_with_max_average} with average grade {max_average:.2f}")
