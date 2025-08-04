import csv
import json
import os

from .exercise import Exercise
from .session import Session

class Data_Manager:

    def __init__(self, sessions: list = None):
        self.sessions = []
        self.restore_previous_sessions()

    def add_session(self, session: Session):
        self.sessions.append(session)

    def write_sessions(self):
        filename = "data.csv"
        if not self.sessions:
            print("No sessions to write")
            return
        
        file_exists = os.path.exists(filename)
        
        with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['name', 'notes', 'type', 'exercises', 'exercise_counter']
            
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            if not file_exists or os.path.getsize(filename) == 0:
                writer.writeheader()
            
            for session in self.sessions:
                session_data = {
                    'name': session.name,
                    'notes': session.notes,
                    'type': session.type,
                    'exercises': json.dumps([ex.to_dict() for ex in session.exercises]),
                    'exercise_counter': session.exercise_counter
                }
                writer.writerow(session_data)

        self.sessions = []

    def restore_previous_sessions(self):
        filename = "data.csv"
        if not os.path.exists(filename):
            return
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                session = Session(
                    name=row['name'],
                    type=row.get('type'),
                    notes=row.get('notes')
                )
                exercises_data = json.loads(row['exercises']) if row.get('exercises') else []
                for ex_data in exercises_data:
                    exercise = Exercise.from_dict(ex_data)
                    session.add_exercise(exercise)
                session.exercise_counter = int(row.get('exercise_counter', len(session.exercises)))
                self.sessions.append(session)

    def get_all_session(self):
        return self.sessions
    
    def get_num_sessions(self):
        return len(self.sessions)