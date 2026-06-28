from student import Student
from calculation import get_grade_points


class SubjectAkbar(Student, get_grade_points):
    """Combines Student + get_grade_points so self.marks works in calculate_grade_point."""
    def __init__(self, name, num_sub):
        Student.__init__(self, name, num_sub)


name    = input("Enter student name   : ")
num_sub = int(input("Enter num of subjects: "))

Akbar = SubjectAkbar(name, num_sub)

total_grade_points = 0.0

print("\n--- Subject Results ---")
for i in range(num_sub):
    print(f"\nSubject {i + 1}:")
    sub_name    = input("  Enter subject name : ")
    Akbar.marks = int(input("  Enter marks (0-100): "))

    Akbar.calculate_grade_point()          
    letter = Akbar.get_letter_grade()
    gpa    = Akbar.get_subject_gpa()

    Akbar.get_data(sub_name, Akbar.marks, gpa)   

    total_grade_points += gpa
    print(f"  {name} got {gpa:.2f} ({letter}) in {sub_name}")

overall_gpa = total_grade_points / num_sub
print(f"\n--- Overall GPA: {overall_gpa:.2f} ---")