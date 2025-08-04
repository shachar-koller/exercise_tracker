from .exercise import Exercise

class Session:

    def __init__(self, name: str, type: str= None, notes: str = None):
        self.name = name
        self.notes = notes
        self.exercises = []
        self.exercise_counter = 0
        self.type = type

    def add_exercise(self, exercise: Exercise):
        self.exercises.append(exercise)
        self.exercise_counter += 1

    def remove_exercise(self, exercise: Exercise):
        self.exercises.remove(exercise)
        self.exercise_counter -= 1

    def add_note(self, note: str):
        self.notes = note

    def clear_note(self):
        self.notes = ""

    def set_type(self, type: str):
        self.type = type

    def get_all_exs(self):
        return [exercise.name for exercise in self.exercises]