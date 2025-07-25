import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from classes.exercise import Exercise
from classes.session import Session

def main():
    test_session = Session(input("Input a date here "))
    exercise1 = Exercise()
    exercise1.getCLIdata()
    test_session.add_exercise(exercise1)
    print(exercise1.name)
    print(exercise1.sets)


if __name__ == "__main__":
    main()