initial_students = (
    "Alice", "Bob", "Charlie",
    "Eve", "Fred", "Ginny", "Harriet",
    "Ileana", "Joseph", "Kincaid", "Larry",
)

seeds = {
    "G": "Grass",
    "C": "Clover",
    "R": "Radishes",
    "V": "Violets",
}


class Garden:
    def __init__(self, diagram, students=initial_students):
        self.diagram = diagram
        self.students = sorted(students)

    def plants(self, name):
        global seeds
        first_row, second_row = self.diagram.split()
        doubles_first = [first_row[i:i+2] for i in range(0, len(first_row), 2)]
        doubles_second = [second_row[i:i+2] for i in range(0, len(second_row), 2)]
        plant_letters = doubles_first[self.students.index(name)] + doubles_second[self.students.index(name)]
        return [seeds[i] for i in plant_letters]
