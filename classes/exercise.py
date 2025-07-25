class Exercise:

    def __init__(self, name: str = None, sets: list = None):
        self.name = name
        self.sets = []


    def getCLIdata(self):
        name1 = input("what exercise did you do? ")
        self.name = name1
        setnum = input("how many sets did you do ")
        inputsets = []
        for i in range(int(setnum)):
            resultpartone = input("what weight? ")
            resultparttwo = input("how many reps ")
            resultpartthree = resultpartone + ", " + resultparttwo
            inputsets.append(resultpartthree)
        self.sets.append(inputsets)
        print("done")