from scacchiera import Scacchiera
import curses

class ScacchieraNC(Scacchiera):
    def __init__(self, screen, r, c):
        Scacchiera.__init__(self, r, c)
        self.screen = screen

    def stampa(self, rig, col):
	for i in range(0,self.r*4+1,4):
		self.screen.addstr(rig+i,col,"-"*(self.r*4))
        for i in range(0,self.c*4+1,4):
            for j in range(0,self.c*4+1,1):
                self.screen.addstr(rig+j,col+i,"|")   
        for i in range(0,self.c*4+1,4):
            for j in range(0,self.c*4+1,4):
                self.screen.addstr(rig+j,col+i,"+")   

