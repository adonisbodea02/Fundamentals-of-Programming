class Person:

    def __init__(self, ID, immunization, status):
        self.ID = ID
        self.immunization = immunization
        self.status = status

    def getID(self):
        return self.ID

    def getImmunization(self):
        return self.immunization

    def getStatus(self):
        return self.status

    def setImmunization(self, new):
        self.immunization = new

    def setStatus(self, new):
        self.status = new

    def __str__(self):
        return "ID: " + str(self.ID) + " Immunization status: " + self.immunization + " Status: " + self.status

class Day:

    def __init__(self, count):
        self.count = count

def readPerfromLine(line):
    line = line.split(",")
    ID = line[0]
    immunization = line[1]
    status = line[2]
    Per = Person(ID, immunization, status)
    return Per

def writePertoLine(el):
    string = str(el.getID()) + "," + self.immunization + "," + self.status
    return string

