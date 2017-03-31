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

      # for i in range(2,self.r*4,4):
          # for j in range(2,self.c*4,4):
              # self.screen.addstr(rig+i,col+j,"x")
        
        for i in range(1,self.r*4,4):
            self.screen.addstr(self.rig+i+1,self.col-1,str(i/4))
        
        for j in range(1,self.c*4,4):
            self.screen.addstr(self.rig-1,self.col+j+1,str(j/4)) 

    def stampa_navi(self):
        for posizione in self.posizioni: 
            self.screen.addstr(posizione[0]+self.rig+2*4,posizione[1]+self.col+2*4,"x")
        

