# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Yiko"
__date__ = "$2-Mar-2015 10:34:11 AM$"

from Map import *
from Node import *
from Cell import *

class Robot:
    
    def __init__(self):
        self.X = 1
        self.Y = 1
        self.Range = 1
        self.Dir = 'U'
        "empty memory for robot"
        self.Memory = Map(15,20)
        self.XGoal = 13
        self.YGoal = 18
        self.XStart = 1
        self.YStart = 1
        self.turnedRight = False
        self.turnedAround = False
        self.turnedLeft = False
        self.StartNode = Node(self.XStart, self.YStart)
        self.GoalNode = Node(self.XGoal, self.YGoal)
        "self.ShortestPath = Node[]"

    def __init__(self, x, y, r, d):
        self.X = x
        self.Y = y
        self.turnedRight = False
        self.turnedAround = False
        self.turnedLeft = False
        self.Range = r
        self.Dir = d
        self.lastDir = ''
        "empty memory for robot"
        self.Memory = Map(15,20)
        self.XGoal = 13
        self.YGoal = 18
        self.XStart = 1
        self.YStart = 1
        self.StartNode = Node(self.XStart, self.YStart)
        self.GoalNode = Node(self.XGoal, self.YGoal)
        "self.ShortestPath = Node[]"

    def turnLeft(self):
        if self.Dir=='U':
            self.Dir = 'L'
            self.lastDir = 'U' 
            turnedLeft = True
        elif self.Dir=='D':
            self.Dir = 'R'
            self.lastDir = 'D' 
            turnedLeft = True
            
        elif self.Dir== 'R':
            self.Dir = 'U'
            self.lastDir = 'R' 
            turnedLeft = True
            
        elif self.Dir== 'L':
            self.Dir = 'D'
            self.lastDir = 'L' 
            turnedLeft = True
            
 
                
    def turnRight(self):  
        if self.Dir== 'U':
            self.Dir = 'R'
            self.lastDir = 'U'
            self.turnedRight = True
            
        elif self.Dir== 'D':
            self.Dir = 'L'
            self.lastDir = 'D' 
            self.turnedRight = True
            
        elif self.Dir== 'R':
            self.Dir = 'D'
            self.lastDir = 'R' 
            self.turnedRight = True
            
        elif self.Dir== 'L':
            self.Dir = 'U'
            self.lastDir = 'L' 
            self.turnedRight = True

    def moveForward(self,dis):
        if self.Dir== 'U':
            self.Y+=dis

        elif self.Dir== 'D':
            self.Y-=dis
            
        elif self.Dir== 'R':
            self.X+=dis
            
        elif self.Dir== 'L':
            self.X-=dis
            
 


    def turnAround(self):
        if self.Dir == 'U':
            self.Dir = 'D'
            self.lastDir = 'U'
            self.turnedAround = True
            
        elif self.Dir== 'D':
            self.Dir = 'U'
            self.lastDir = 'D' 
            self.turnedAround = True
            
        elif self.Dir== 'R':
            self.Dir = 'L'
            self.lastDir = 'R'
            self.turnedAround = True

        elif self.Dir== 'L':
            self.Dir = 'R'
            self.lastDir = 'L'
            self.turnedAround = True
            
    def explore(self,ArStr):
        print "Current X= ", self.X, " Current Y = ", self.Y
        try:
            isBlockedLeft = self.checkLeftSide(ArStr)
            isBlockedFront = self.checkTopSide(ArStr)
            isBlockedRight = self.checkRightSide(ArStr)
            if (not isBlockedRight && !turnedRight):
                print("Turn right")
                self.turnRight()
                return "2"
            elif (not isBlockedFront):
                print("Move Forward")
                self.moveForward(1)
                self.turnedRight = False
                return "1"
            elif (not isBlockedLeft):
                print("turn left")
                self.turnedRight = False
                self.turnLeft()
                return "3"
            else:
                print("Turn around")
                self.turnAround()
                self.turnedRight = False
                return "4"
        except ValueError as e:
            print(e.Message)
            print(e)
        print 
    
    def checkLeftSide(self, ArStr):
        print self.Dir
        isBlocked = False
        if self.Dir == 'R':
            isBlocked = checkTop()
        if self.Dir == 'U':
            isBlocked = checkLeft()
        if self.Dir == 'L':
            isBlocked = checkBottom()
        if self.Dir == 'D':
            isBlocked = checkRight()
        #x = self.X - self.Range - 1
        if (ArStr[0] == '1'):
            isBlocked = True
            #explored and has obstacle
            updateMap(0, 1)
        else:
            #empty cell
            updateMap(0, 2)
        print "Left", isBlocked
        return isBlocked
    
    def checkTopSide(self, ArStr):
        isBlocked = False
        if self.Dir == 'R':
            isBlocked = checkRight()
        if self.Dir == 'U':
            isBlocked = checkTop()
        if self.Dir == 'L':
            isBlocked = checkLeft()
        if self.Dir == 'D':
            isBlocked = checkBottom()
        for i in range(1,4):
            if (ArStr[i]=='1'):
                isBlocked = True
                #explored and has obstacle 
                updateMap(i, 1)
            else:
                #empty 
                updateMap(i, 2)
        print "TOP", isBlocked
        return isBlocked

    def checkRightSide(self, ArStr):
        isBlocked = False
        if self.Dir == 'R':
            isBlocked = checkBottom()
        if self.Dir == 'U':
            isBlocked = checkRight()
        if self.Dir == 'L':
            isBlocked = checkTop()
        if self.Dir == 'D':
            isBlocked = checkLeft()
        for i in range(4,7):
            if (ArStr[i] == '1'):
                isBlocked = True
                #explored and has obstacle 
                updateMap(i, 1)
            else:
                #empty
                updateMap(i, 2)
        print "RIGHT ", isBlocked
        return isBlocked

    #not done
    def updateMap(self, pos, val):
        if(self.Dir == 'U'):
            if(pos == 0):
                self.Memory.grid[self.X - 2][self.Y + 1] = val
            if(pos == 1):
                self.Memory.grid[self.X - 1][self.Y + 2] = val
            if(pos == 2):
                self.Memory.grid[self.X][self.Y + 2] = val
            if(pos == 3):
                self.Memory.grid[self.X + 1][self.Y + 2] = val
            if(pos == 4):
                self.Memory.grid[self.X + 2][self.Y + 1] = val
            if(pos == 5):
                self.Memory.grid[self.X + 2][self.Y] = val
            if(pos == 6):
                self.Memory.grid[self.X + 2][self.Y - 1] = val
        elif(self.Dir == 'R'):
            if(pos == 0):
                self.Memory.grid[self.X + 1][self.Y + 2] = val
            if(pos == 1):
                self.Memory.grid[self.X + 2][self.Y + 1] = val
            if(pos == 2):
                self.Memory.grid[self.X + 2][self.Y] = val
            if(pos == 3):
                self.Memory.grid[self.X + 2][self.Y - 1] = val
            if(pos == 4):
                self.Memory.grid[self.X + 1][self.Y - 2] = val
            if(pos == 5):
                self.Memory.grid[self.X][self.Y - 2] = val
            if(pos == 6):
                self.Memory.grid[self.X - 1][self.Y - 2] = val
        elif(self.Dir == 'D'):
            if(pos == 0):
                self.Memory.grid[self.X + 2][self.Y - 1] = val
            if(pos == 1):
                self.Memory.grid[self.X + 1][self.Y - 2] = val
            if(pos == 2):
                self.Memory.grid[self.X][self.Y - 2] = val
            if(pos == 3):
                self.Memory.grid[self.X - 1][self.Y - 2] = val
            if(pos == 4):
                self.Memory.grid[self.X - 2][self.Y - 1] = val
            if(pos == 5):
                self.Memory.grid[self.X - 2][self.Y] = val
            if(pos == 6):
                self.Memory.grid[self.X - 2][self.Y + 1] = val
        elif(self.Dir == 'L'):
            if(pos == 0):
                self.Memory.grid[self.X - 1][self.Y - 2] = val
            if(pos == 1):
                self.Memory.grid[self.X - 2][self.Y - 1] = val
            if(pos == 2):
                self.Memory.grid[self.X - 2][self.Y] = val
            if(pos == 3):
                self.Memory.grid[self.X - 2][self.Y + 1] = val
            if(pos == 4):
                self.Memory.grid[self.X - 1][self.Y + 2] = val
            if(pos == 5):
                self.Memory.grid[self.X][self.Y + 2] = val
            if(pos == 6):
                self.Memory.grid[self.X + 1][self.Y + 2] = val

    def checkTop(self):
        if(self.Y + self.Range + 1 >= self.Memory.height):
            return True
        if(self.Memory.grid[self.X -1][self.Y + 2] == 1):
            return True
        if(self.Memory.grid[self.X][self.Y + 2] == 1):
            return True
        if(self.Memory.grid[self.X + 1][self.Y + 2] == 1):
            return True
        return False
    def checkLeft(self):
        if(self.X - self.Range - 1 < 0):
            return True
        if(self.Memory.grid[self.X - 2][self.Y + 1] == 1):
            return True
        if(self.Memory.grid[self.X - 2][self.Y] == 1):
            return True
        if(self.Memory.grid[self.X - 2][self.Y -1 ] == 1):
            return True
        return False
    def checkRight(self):
        if(self.X + self.Range + 1 >= self.Memory.width):
            return True
        if(self.Memory.grid[self.X + 2][self.Y + 1] == 1):
            return True
        if(self.Memory.grid[self.X+2][self.Y] == 1):
            return True
        if(self.Memory.grid[self.X + 2][self.Y -1] == 1):
            return True
        return False
    def checkBottom(self):
        if(self.Y - self.Range - 1 >= self.Memory.height):
            return True
        if(self.Memory.grid[self.X -1][self.Y - 2] == 1):
            return True
        if(self.Memory.grid[self.X][self.Y - 2] == 1):
            return True
        if(self.Memory.grid[self.X + 1][self.Y - 2] == 1):
            return True
        return False