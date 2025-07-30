import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from classes.exercise import Exercise
from classes.session import Session

def main():
    test_session = Session("12/19/2004")
    exercise1 = Exercise("Bench Press")
    exercise1.add_set(weight=115, reps=3)
    exercise1.add_set(weight=115, reps=4)
    exercise1.add_set(weight=115, reps=3)
    test_session.add_exercise(exercise1)
    print(exercise1.toRedisString())


if __name__ == "__main__":
    main()