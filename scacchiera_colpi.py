from scacchiera_generale import *

class ScacchieraColpi(ScacchieraGenerale):
    def __init__(self,r,c):
        ScacchieraGenerale.__init__(self,r,c)

    def posizione_colpi(self,posizione):
        if posizione[0] < 0 or posizione[1] < 0 or posizione[1] > self.r or posizione[1] > self.c:
            return
        else:
            self.posizioni.append(posizione)
