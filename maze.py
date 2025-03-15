import math
             
class Maze:
    
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.uniquePath = ""
        self.count = 0
        self.visited = {}
        self.paths = []
        self.move(x1, y1, x2, y2, self.uniquePath)
    
    def __str__(self):
        result = ""
        for item in reversed(self.paths):
            result += f"{item}\n"
        result += f"Number of paths: {self.count}"
        return result

    def goEast(self, x1, y1, x2):
        if (x1 + 1, y1) not in self.visited and x1 < x2:
            self.visited[(x1 + 1, y1)] = True
            return True
        return False
        
    def goWest(self, x1, y1, x2):
        if (x1 - 1, y1) not in self.visited and x1 > x2:
            self.visited[(x1 - 1, y1)] = True
            return True
        return False

    def goNorth(self, x1, y1, y2):
        if (x1, y1 + 1) not in self.visited and y1 < y2:
            self.visited[(x1, y1 + 1)] = True
            return True
        return False

    def goSouth(self, x1, y1, y2):
        if (x1, y1 - 1) not in self.visited and y1 > y2:
            self.visited[(x1, y1 - 1)] = True
            return True
        return False
        
    def move(self, x1, y1, x2, y2, uniquePath):
        if (x1 == x2 and y1 == y2):
            self.count += 1
            self.paths.append(uniquePath)
        
        self.visited[(x1, y1)] = True
        
        if self.goEast(x1, y1, x2):
            self.move(x1 + 1, y1, x2, y2, uniquePath + "E")
        
        if self.goWest(x1, y1, x2):
            self.move(x1 - 1, y1, x2, y2, uniquePath + "W")
        
        if self.goNorth(x1, y1, y2):
            self.move(x1, y1 + 1, x2, y2, uniquePath + "N")
        
        if self.goSouth(x1, y1, y2):
            self.move(x1, y1 - 1, x2, y2, uniquePath + "S")
        
        del self.visited[(x1, y1)]


            
               
        
            