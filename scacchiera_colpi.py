from scacchiera_generale import *

class ScacchieraColpi(ScacchieraGenerale):
    def __init__(self,r,c):
        ScacchieraGenerale.__init__(self,r,c)
        self.colpite=[]

    def posizione_colpi(self,posizione,x):
        
        if posizione[0] <= 0 or posizione[1] <= 0 or posizione[1] > self.r or posizione[1] > self.c:
            return
        

        else:
            if x==True:
                self.colpite.append(posizione)
            else: 
                self.posizioni.append(posizione)
