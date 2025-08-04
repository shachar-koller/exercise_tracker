import json

class Exercise:

    def __init__(self, name: str = None, sets: list = None):
        self.name = name
        self.sets = sets if sets is not None else []

    def add_set(self, weight: float, reps: int):
        set_data = {
            "weight": weight,
            "reps": reps
        }
        self.sets.append(set_data)
    
    def to_dict(self):
        return {
            "name": self.name,
            "sets": self.sets
        }
    
    @classmethod
    def from_dict(cls, data):
        exercise = cls(name=data.get("name"))
        exercise.sets = data.get("sets", [])
        return exercise
    
    def __str__(self):
        return f"Exercise: {self.name}, Sets: {self.sets}"

    def getCLIdata(self):
        name1 = input("what exercise did you do? ")
        self.name = name1
        setnum = input("how many sets did you do ")
        for i in range(int(setnum)):
            weight = input("what weight? ")
            reps = input("how many reps ")
            set_data = {
                "weight": float(weight) if weight else 0.0,
                "reps": int(reps) if reps else 0
            }
            self.sets.append(set_data)
        print("done")