from scacchiera_generale import *

class ScacchieraColpi(ScacchieraGenerale):
    def __init__(self,r,c):
        ScacchieraGenerale.__init__(self,r,c)

    def posizione_colpi(self,posizione):
        self.posizioni.append(posizione)
