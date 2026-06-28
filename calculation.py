class get_grade_points:

    def calculate_grade_point(self):
            if self.marks >= 85:
                self.grade_point = 4.0
            elif self.marks >= 80:
                self.grade_point = 3.67
            elif self.marks >= 75:
                self.grade_point = 3.33
            elif self.marks >= 70:
                self.grade_point = 3.00
            elif self.marks >= 65:
                self.grade_point = 2.67
            elif self.marks >= 61:
                self.grade_point = 2.33
            elif self.marks >= 58:
                self.grade_point = 2.00
            elif self.marks >= 55:
                self.grade_point = 1.67
            elif self.marks >= 53:
                self.grade_point = 1.33    
            elif self.marks >= 50:
                self.grade_point = 1.00   
            else:
                self.grade_point = 0.0

    def get_letter_grade(self):
        if self.grade_point == 4.0:
            return "A+"
        elif self.grade_point == 3.67:
            return "A-"
        elif self.grade_point == 3.33:
            return "B+"
        elif self.grade_point == 3.00:
            return "B"
        elif self.grade_point == 2.67:
                return "B-"
        elif self.grade_point == 2.33:
                return "C+"
        elif self.grade_point == 2.00:
                return "C"
        elif self.grade_point == 1.67:
                return "C-"
        elif self.grade_point == 1.33:
                return "D+"
        elif self.grade_point == 1.00:
                return "D"
        else:
            return "F"

    def get_subject_gpa(self):
        return self.grade_point
        
        
        
        