from scacchiera_generale import *

class ScacchieraNavi(ScacchieraGenerale):
    def __init__(self,r,c):
        ScacchieraGenerale.__init__(self,r,c)
        self.pos_nn_accet=[]

    def posizione_nave(self,posizione,grande,verso):
        if grande==1:
            if posizione[0]>self.r or posizione[0]<0 or posizione[1]>self.c or posizione[1]<0 or (posizione[0], posizione[1]) in self.pos_nn_accet:
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

        elif grande==2 and verso=="h":
            if posizione[0]>self.r or posizione[0]<0 or posizione[1]>=self.c or posizione[1]<0 or (posizione[0], posizione[1]) in self.pos_nn_accet or (posizione[0],posizione[1]+1) in self.pos_nn_accet:
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

        elif grande==2 and verso=="v":
            if posizione[0]>=self.r or posizione[0]<0 or posizione[1]>self.c or posizione[1]<0 or (posizione[0], posizione[1]) in self.pos_nn_accet or (posizione[0]+1,posizione[1]) in self.pos_nn_accet:
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




if __name__=='__main__':
    s = ScacchieraNavi(5, 5)
    print s
    print type(s)
    print type(s) is ScacchieraNavi
    print isinstance(s, ScacchieraNavi)
