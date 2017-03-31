class Scacchiera:
    def __init__(self, r, c):
        self.r=r
        self.c=c
        self.posizioni=[]
    def posizione_nave(self,posizione):
        for posizione in self.posizioni:
            if(posizione[0] > sel.r or posizione[0] < 0 or posizione[1] > self.c or posizione[1] < 0):
                return
            else:
                self.posizioni.append(posizione)
    
                        
        
    

