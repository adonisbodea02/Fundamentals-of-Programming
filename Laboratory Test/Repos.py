import Domains

class PersonRepoFile:

    def __init__(self, readPerfromLine, fname):
        self.read = readPerfromLine
        self.fname = fname
        self.data = []

    def readAllfromFile(self):

        with open(self.fname, 'r') as f:
            lines = f.readlines()
            List = []
            for line in lines:
                line = line.strip()
                if len(line) > 1:
                    Per = self.read(line)
                    List.append(Per)
            f.close()
            return List

    def getAll(self):
        return self.data

    def findByID(self, ID):
        for i in range(len(self.data)):
            if self.data[i].getID() == ID:
                return ID
        return None

    def add(self, per):
        self.data.append(per)

