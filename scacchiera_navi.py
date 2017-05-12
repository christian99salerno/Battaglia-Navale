from scacchiera_generale import *

class ScacchieraNavi(ScacchieraGenerale):
    maxnavi=7
   
    def __init__(self,r,c):
        ScacchieraGenerale.__init__(self,r,c)
        self.pos_nn_accet=[]
        self.navi_abbattute=[]
        self.cbreak=0
        self.navi1max=3
        self.navi2max=2

    def posizione_nave(self,posizione,grande,verso):
        
        if grande==1:
            if posizione[0]>self.r or posizione[0]<=0 or posizione[1]>self.c or posizione[1]<=0 or (posizione[0], posizione[1]) in self.pos_nn_accet or self.navi1max==0:
                return
            else:
                self.posizioni.append(posizione)
                self.pos_nn_accet.append((posizione[0],posizione[1]))
                self.pos_nn_accet.append((posizione[0],posizione[1]-1))
                self.pos_nn_accet.append((posizione[0],posizione[1]+1))
                self.pos_nn_accet.append((posizione[0]-1,posizione[1]))
                self.pos_nn_accet.append((posizione[0]-1,posizione[1]+1))
                self.pos_nn_accet.append((posizione[0]-1,posizione[1]-1))
                self.pos_nn_accet.append((posizione[0]+1,posizione[1]))
                self.pos_nn_accet.append((posizione[0]+1,posizione[1]-1))
                self.pos_nn_accet.append((posizione[0]+1,posizione[1]+1))
                self.navi1max-=1

        elif grande==2 and verso=="h":
            if posizione[0]>self.r or posizione[0]<=0 or posizione[1]>=self.c or posizione[1]<=0 or (posizione[0], posizione[1]) in self.pos_nn_accet or (posizione[0],posizione[1]+1) in self.pos_nn_accet or self.navi2max==0:
                return
            else:
                self.posizioni.append(posizione)
                self.posizioni.append((posizione[0],posizione[1]+1))
                self.pos_nn_accet.append((posizione[0],posizione[1]))
                self.pos_nn_accet.append((posizione[0],posizione[1]-1))
                self.pos_nn_accet.append((posizione[0],posizione[1]+1))
                self.pos_nn_accet.append((posizione[0]-1,posizione[1]))
                self.pos_nn_accet.append((posizione[0]-1,posizione[1]+1))
                self.pos_nn_accet.append((posizione[0]-1,posizione[1]-1))
                self.pos_nn_accet.append((posizione[0]+1,posizione[1]))
                self.pos_nn_accet.append((posizione[0]+1,posizione[1]-1))
                self.pos_nn_accet.append((posizione[0]+1,posizione[1]+1))
                self.pos_nn_accet.append((posizione[0],posizione[1]+2))
                self.pos_nn_accet.append((posizione[0]+1,posizione[1]+2))
                self.pos_nn_accet.append((posizione[0]-1,posizione[1]+2))
                self.navi2max-=1

        elif grande==2 and verso=="v":
            if posizione[0]>=self.r or posizione[0]<=0 or posizione[1]>self.c or posizione[1]<=0 or (posizione[0], posizione[1]) in self.pos_nn_accet or (posizione[0]+1,posizione[1]) in self.pos_nn_accet or self.navi2max==0:
                return
            else:
                self.posizioni.append(posizione)
                self.posizioni.append((posizione[0]+1,posizione[1]))
                self.pos_nn_accet.append((posizione[0],posizione[1]))
                self.pos_nn_accet.append((posizione[0],posizione[1]-1))
                self.pos_nn_accet.append((posizione[0],posizione[1]+1))
                self.pos_nn_accet.append((posizione[0]-1,posizione[1]))
                self.pos_nn_accet.append((posizione[0]-1,posizione[1]+1))
                self.pos_nn_accet.append((posizione[0]-1,posizione[1]-1))
                self.pos_nn_accet.append((posizione[0]+1,posizione[1]))
                self.pos_nn_accet.append((posizione[0]+1,posizione[1]-1))
                self.pos_nn_accet.append((posizione[0]+1,posizione[1]+1))
                self.pos_nn_accet.append((posizione[0]-2,posizione[1]-1))
                self.pos_nn_accet.append((posizione[0]-2,posizione[1]))
                self.pos_nn_accet.append((posizione[0]-2,posizione[1]+1))
                self.navi2max-=1

    def BreakShip(self, colpo):
        if self.cbreak==ScacchieraNavi.maxnavi or colpo[0] > self.r or colpo[1] > self.c or colpo[0] <= 0 or colpo[1] <= 0:
            return 0
        else:
            if colpo in self.posizioni:
               self.navi_abbattute.append(colpo)
               self.cbreak+=1
               return 1
            else:                   
               return 0
             


