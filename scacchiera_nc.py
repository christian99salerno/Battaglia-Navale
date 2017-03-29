from scacchiera import *
import curses

class ScacchieraNC(Scacchiera):
    def __init__(self, screen, r, c):
        Scacchiera.__init__(self, r, c)
        self.screen = screen

    def stampa(self, rig, col):
	for i in range(0,self.r*4+1,4):
		self.screen.addstr(rig+i,col,"-"*(self.c*4))
        for i in range(0,self.c*4+1,4):
            for j in range(0,self.r*4+1,1):
                self.screen.addstr(rig+j,col+i,"|")   
        for i in range(0,self.r*4+1,4):
            for j in range(0,self.c*4+1,4):
                self.screen.addstr(rig+i,col+j,"+")   

        for i in range(2,self.r*4,4):
            for j in range(2,self.c*4,4):
                self.screen.addstr(rig+i,col+j,"x")
        
    def stampa_navi(self):
        for i in range(-1,self.r*4,4):
            for j in range(1,self.r,1):
                self.screen.addstr(self.rig+i,self.col,str(j))
        #for j in range(2,self.c*4,4):

    #def stampa_navi(self):
        #for posizione in self.posizioni:
