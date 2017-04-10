from scacchiera import *
import curses

class ScacchieraNC(Scacchiera):
    def __init__(self, screen, r, c, rig, col):
        Scacchiera.__init__(self, r, c)
        self.screen = screen
        self.rig=rig
        self.col=col

    def stampa(self):
	for i in range(0,self.r*4+1,4):
		self.screen.addstr(self.rig+i,self.col,"-"*(self.c*4))
        
        for i in range(0,self.c*4+1,4):
            for j in range(0,self.r*4+1,1):
                self.screen.addstr(self.rig+j,self.col+i,"|")   
        
        for i in range(0,self.r*4+1,4):
            for j in range(0,self.c*4+1,4):
                self.screen.addstr(self.rig+i,self.col+j,"+")   
        
        for righe in range(1,self.r+1):
            self.screen.addstr(self.rig+2+4*(righe-1), self.col-1,  str(righe))
        
        for colonne in range(1, self.c+1):
            self.screen.addstr(self.rig-1, self.col+2+4*(colonne-1), str(colonne))
        
    def stampa_navi(self):
        for posizione in self.posizioni: 
            self.screen.addstr((self.rig+2)+4*(posizione[0]-1),(self.col+2)+4*(posizione[1]-1),"x")
        
