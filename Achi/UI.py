from Domain import Board,AI,Player

class UI():

    @staticmethod
    def PrintMenu():
        string = "Choose one of the following: \n"
        string += "1.Start a new game \n"
        string += "2.Continue an old one \n"
        string += "0.Exit"
        print(string)

    @staticmethod
    def ValidCommands(command):
        availableCommands = ['1', '2', '0']
        return command in availableCommands

    @staticmethod
    def checkinteger(msg):

        if msg.isdigit():
            return int(msg)
        return "fals"


    def NewGame(self):
        b = Board()
        ai = AI("O")

        print(b)

        while b.iswon("X") == False and b.iswon("O") == False:
            line = input("Choose your line: ")
            column = input("Choose your column: ")
            while(self.checkinteger(line) == "fals"):
                print("Line is not an integer!")
                line = input("Choose your line: ")
            line = self.checkinteger(line)
            while(self.checkinteger(column) == "fals"):
                print("Column is not an integer!")
                column = input("Choose your column: ")
            column = self.checkinteger(column)
            while b.move(line, column, "X") == False:
                print("Please give adequate coordinates!")
                line = input("Choose your line: ")
                column = input("Choose your column: ")
                if (self.checkinteger(line) != "fals"):
                    line = self.checkinteger(line)
                    if (self.checkinteger(column) != "fals"):
                        column = self.checkinteger(column)
                    else:
                        print("The column is not an integer!")
                else:
                    print("The line is not an integer!")
            print(b)
            if b.iswon("X") == True:
                print(b)
                print("You win!")
                break
            if(b.placementfinished() == True):
                print(b)
                break
            ai.move(b)
            if b.iswon("O") == True:
                print(b)
                print("Computer wins!")
                break
            if (b.placementfinished() == True):
                print(b)
                break
            print(b)
            print("Do you want to save the game?")
            decision = input()
            if decision == "Yes":
                b.writeToFile("BoardFile")
                break

        # if b.iswon("X") == True:
        #     print("You win!")
        #
        # if b.iswon("O") == True:
        #     print("Computer wins!")

        print("\n")
        print("\n")

    def OldGame(self):
        b = Board()
        ai = AI("O")

        b.readFromFile("BoardFile")

        print(b)

        while b.iswon("X") == False and b.iswon("O") == False:
            line = input("Choose your line: ")
            column = input("Choose your column: ")
            while (self.checkinteger(line) == "fals"):
                print("Line is not an integer!")
                line = input("Choose your line: ")
            line = self.checkinteger(line)
            while (self.checkinteger(column) == "fals"):
                print("Column is not an integer!")
                column = input("Choose your column: ")
            column = self.checkinteger(column)
            while b.move(line, column, "X") == False:
                print("Please give adequate coordinates!")
                line = input("Choose your line: ")
                column = input("Choose your column: ")
                if (self.checkinteger(line) != "fals"):
                    line = self.checkinteger(line)
                    if (self.checkinteger(column) != "fals"):
                        column = self.checkinteger(column)
                    else:
                        print("The column is not an integer!")
                else:
                    print("The line is not an integer!")
            print(b)
            if b.iswon("X") == True:
                print(b)
                print("You win!")
                break
            if (b.placementfinished() == True):
                print(b)
                break
            ai.move(b)
            if b.iswon("O") == True:
                print(b)
                print("Computer wins!")
                break
            if (b.placementfinished() == True):
                print(b)
                break
            print(b)
            print("Do you want to save the game?")
            decision = input()
            if decision == "Yes":
                b.writeToFile("BoardFile")
                break

        # if b.iswon("X") == True:
        #     print("You win!")
        #
        # if b.iswon("O") == True:
        #     print("Computer wins!")

        print("\n")
        print("\n")

    def MainMenu(self):
        commandDict = {'1': self.NewGame,
                       '2': self.OldGame}
        while True:
            UI.PrintMenu()
            command = input("Please choose: ")
            while not UI.ValidCommands(command):
                command = input("Please type a valid command!")
            if command == '0':
                break
            commandDict[command]()
