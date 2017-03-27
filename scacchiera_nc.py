from scacchiera import Scacchiera
import curses

class ScacchieraNC(Scacchiera):
    def __init__(self, r, c):
        Scacchiera.__init__(self, r, c)
    
    def stampa(self, screen, rig, col):
        for i in range (0,self.r*4,4):
            self.screen.addstr(rig,col+i,"-"*(self.r*4))

            
