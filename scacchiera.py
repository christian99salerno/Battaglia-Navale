class Scacchiera:
    def __init__(self, r, c):
        self.r=r
        self.c=c
        self.posizioni=[]
        self.pos_nn_accet=[]

    def posizione_nave(self,posizione):
        if(posizione[0] > self.r or posizione[0] < 0 or posizione[1] > self.c or posizione[1] < 0):
            return
        else:
            self.posizioni.append(posizione)
        
            self.pos_nn_accet.append((posizione[0],posizione[1]))
            self.pos_nn_accet.append((posizione[0],posizione[1]-1))
            self.pos_nn_accet.append((posizione[0],posizione[1]+1))
            self.pos_nn_accet.append((posizione[0]-1,posizione[1]))
            self.pos_nn_accet.append((posizione[0]-1,posizione[1]+1))
            self.pos_nn_accet.append((posizione[0]-1,posizione[0]-1))
            self.pos_nn_accet.append((posizione[0]+1,posizione[1]))
            self.pos_nn_accet.append((posizione[0]+1,posizione[1]-1))
            self.pos_nn_accet.append((posizione[0]+1,posizione[1]+1))
        
        if posizione[0] in self.pos_nn_accett == True and posizione[1] in self.pos_nn_accett == True:
            return
