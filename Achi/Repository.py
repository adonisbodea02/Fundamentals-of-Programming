class BoardRepo:

    def __init__(self, fname):
        self.fname = fname
        self.data = []

    def readFromFile(self):

        with open(self.fname, 'r') as f:
            boarddata = []
            lines = f.readlines()
            for line in lines:
                dataline = []
                for i in range(3):
                    if line[i] == "+":
                        dataline.append(" ")
                    elif line[i] == "X":
                        dataline.append("X")
                    elif line[i] == "O":
                        dataline.append("O")
                boarddata.append(dataline[:])




