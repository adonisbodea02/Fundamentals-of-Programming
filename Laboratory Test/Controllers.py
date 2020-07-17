from Domains import Person
from Domains import readPerfromLine
from Repos import PersonRepoFile
import unittest
import sys
sys.path.append('/UBB/1st Year/FP/Laboratory Test')

class PersonController:

    def __init__(self, PerRepo):
        """
        initializer for Persons Controller
        :param PerRepo:
        """
        self.PerRepo = PerRepo

    def getAll(self):
        '''
        function for displaying all people
        '''
        return self.PerRepo.getAll()

    def Vaccinate(self,ID):
        """
        checks if a person can be vaccinated
        param ID
        """
        if self.PerRepo.findByID(ID) != None:
            i = self.PerRepo.findByID(ID)
            if self.PerRepo.data[i].getStatus() == 'healthy':
                self.PerRepo.data[i].setImmunization("vaccinated")
            else:
                return False
        else:
            return None
        return True

def Test():
        Per1 = Person(1,'nonvaccinated','ill')
        Per2 = Person(2,'nonvaccinated', 'healthy')
        PerRepo = PersonRepoFile(readPerfromLine,'person.txt')
        PerRepo.add(Per1)
        PerRepo.add(Per2)
        assert len(PerRepo.data) == 2
        ctrl = PersonController(PerRepo)
        ctrl.Vaccinate(1)
        assert ctrl.PerRepo.data[1].getImmunization() == "vaccinated"

Test()


