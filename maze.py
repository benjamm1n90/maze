import math

class Maze:
    
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.path = [[]]
        self.uniquePath = ""
        self.move(x1, y1, x2, y2)
    
    def __str__(self):
        return f"Path: {self.path}"
        
    def move(self, x1, y1, x2, y2):
            i = 0
            if(x1 < x2):
                self.uniquePath += "E"
                self.move(x1 + 1, y1, x2, y2)
            elif(y1 < y2):
                self.uniquePath += "N"
                self.move(x1, y1 + 1, x2, y2)
            elif(x1 > x2):
                self.uniquePath += "W"
                self.move(x1 - 1, y1, x2, y2)
            elif(y1 > y2):
                self.uniquePath += "S"
                self.move(x1, y1 - 1, x2, y2)                                
            else:
                self.path[i].append(self.uniquePath)
                i+=1
                print(self.uniquePath)
            
            
        
            