from Domains import Person
from Domains import readPerfromLine
from Repos import PersonRepoFile
from Controllers import PersonController
from UI import UI
import sys
sys.path.append('/UBB/1st Year/FP/Laboratory Test')

repoPer = PersonRepoFile(readPerfromLine, "people.txt")
List = repoPer.readAllfromFile()
for el in List:
    repoPer.add(el)
perController = PersonController(repoPer)
ui = UI(perController)
ui.MainMenu()