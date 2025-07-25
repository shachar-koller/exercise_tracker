from .exercise import Exercise

class Session:

    def __init__(self, name: str, notes: str = None):
        self.name = name
        self.notes = notes
        self.exercises = []
        self.exercise_counter = 0


    def add_exercise(self, exercise: Exercise):
        self.exercises.append(exercise)
        self.exercise_counter += 1