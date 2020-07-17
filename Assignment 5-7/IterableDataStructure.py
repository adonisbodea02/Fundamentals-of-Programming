from Domain.Discipline import Discipline


class Repo:

    def __init__(self):
        self.__data = []
        self.__index = 0

    def __iter__(self):
        return iter(self.__data)

    def __next__(self):
        if self.__index > len(self.__data):
            raise StopIteration
        self.__index += 1

        return self.__data[self.__index]

    def __setitem__(self, key, value):
        self.__data[key] = value

    def __getitem__(self, item):
        return  self.__data[item]

    def __delitem__(self, key):
        del self.__data[key]

    def __len__(self):
        return len(self.__data)

    def append(self, obj):
        self.__data.append(obj)

    def pop(self, key):
        self.__data.pop(key)

    def getAll(self):
        return self.__data

    def filternewlist(self, newlist):
        self.__data = newlist



DisRepo = Repo()

for i in DisRepo:
    print(i)

d1 = Discipline(1, "Japanese")
d2 = Discipline(2, "Manga")
d3 = Discipline(3, "History")
d4 = Discipline(4, "Game Theory")

DisRepo.append(d1)
DisRepo.append(d2)
DisRepo.append(d4)
DisRepo.append(d3)

#DisRepo.__delitem__(1)
# DisRepo.__setitem__(0, d2)

def GnomeSort(List, cmpfunction):
    pos = 0
    while pos < len(List):
        if(pos == 0 or cmpfunction(List[pos], List[pos-1]) == 1):
            pos += 1
        else:
            t = List[pos]
            List[pos] = List[pos-1]
            List[pos-1] = t
            pos -= 1


def disciplinecmpfunction(dis1, dis2):
    if dis1.getName() > dis2.getName():
        return 1
    return 0


def filter(List, validfunction):

    for el in List:
        if validfunction(el) is True:
            yield el
    #List = [el for el in List if validfunction(el) is True]
    #return List

def AinDis(dis):
    if dis.getName().find('o') != -1:
        return True
    return False








