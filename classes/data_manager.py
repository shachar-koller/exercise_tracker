import csv
import json
import os
from .session import Session

class Data_Manager:

    def __init__(self, sessions: list = None):
        self.sessions = []

    def add_session(self, session: Session):
        self.sessions.append(session)

    def write_sessions(self):
        filename = "data.csv"
        if not self.sessions:
            print("No sessions to write")
            return
        
        file_exists = os.path.exists(filename)
        
        with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['name', 'notes', 'exercises', 'exercise_counter']
            
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            if not file_exists or os.path.getsize(filename) == 0:
                writer.writeheader()
            
            for session in self.sessions:
                session_data = {
                    'name': session.name,
                    'notes': session.notes,
                    'exercises': json.dumps([ex.to_dict() for ex in session.exercises]),
                    'exercise_counter': session.exercise_counter
                }
                writer.writerow(session_data)

        self.sessions = []