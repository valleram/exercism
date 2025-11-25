class School:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        """
        :param name: string
        :type grade: int
        """
        if grade not in self.students:
            self.students[grade] = [name]
        else:
            self.students[grade].append(name)

    def roster(self):
        student_list = []
        sorted_grades = sorted(self.students.keys())
        for i in sorted_grades:
            get_students = self.students[i]
            student_list.extend(sorted(get_students))
        return student_list

    def grade(self, grade_number):
        if self.students:
            return sorted(self.students[grade_number])
        return []
