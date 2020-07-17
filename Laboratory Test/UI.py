class UI:

    def __init__(self, PerController):
        self.Controller = PerController

    @staticmethod
    def printMenu():
        string = "Available commands:\n"
        string += "1. List all people: \n"
        string += "2. Vaccinate a person: \n"
        string += "0. Exit"
        print(string)

    def listall(self):
        for i in self.Controller.getAll():
            print(i)

    def vaccinate(self):
        ID = int(input("Please enter ID: "))
        res = self.Controller.Vaccinate(ID)
        if res == False:
            print("The person is already ill")
        elif res == None:
            print("There is no person with the given ID")

    def MainMenu(self):

        ok = True
        while ok == True:
            UI.printMenu()
            command = input("Please type your command: ")
            if command == '0':
                ok = False
            elif command == '1':
                self.listall()
            elif command == '2':
                self.vaccinate()
