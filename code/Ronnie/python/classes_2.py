class Robot:
    def __init__(self, color, height):
        self.color = color
        self.program = ''
        self.height = height

    def printShinyRobot(self):
        finish = 'shiny'
        print(self.color + ' ' + finish + ' ' + str(self.height))

    def programRobot(self, program):
        self.program = program
        print('This robot is programmed using ' + self.program)
    
    def printRobot(self):
        print(self.color + ',' + self.program + ',' + str(self.height))

shiny_purple = Robot('purple', 5)
shiny_blue = Robot('blue', 4)

shiny_purple.printShinyRobot()
shiny_purple.programRobot('C++')
shiny_purple.printRobot()