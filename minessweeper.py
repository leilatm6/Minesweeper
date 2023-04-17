import random


class Minesweeper: 
    def __init__(self, numcell, nummins):
       self.minecells = set()  
       self.nummins = nummins
       self.numcell = numcell
       while len(self.minecells) < nummins:
            i = random.randint(0, numcell - 1)
            j = random.randint(0, numcell - 1)
            if (i, j) not in self.minecells:
                self.minecells.add((i, j))

    def ismine(self, cell):
        i, j = cell
        if (i,j) in self.minecells:
            return True
        return False
    
    def findmine(self,cell):
        i, j = cell
        if (i,j) in self.minecells:
            self.nummins -= 1

    def remainmine(self):
        if self.nummins == 0:
            return False
        return True
    
    def findneighbors(self, cell):
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1 , -1), (1, 1), (1, -1), (-1, 1)]
        (i, j) = cell
        neighbors = set()
        for (x,y) in directions:
            dx = x + i
            dy = y + j
            if 0 <= dx < self.numcell and 0 <= dy < self.numcell:
                neighbors.add((dx,dy))
        return neighbors
    
"""
def calcute_neighbor_mine(self,cell):
        neighbormine = 0
        neighbors = self.findneighbors(cell)
        for (i,j) in neighbors:
            if (i,j) in self.minecells:
                neighbormine += 1              
        return neighbormine"""
    
    
                
    
        
