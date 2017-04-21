import curses
from scacchiera_navi import *
from scacchiera_colpi import *

def StampaScacchiera(scacchiera, screen, pos_rig, pos_col):
    for i in range(0,scacchiera.r*4+1,4):
	screen.addstr(pos_rig+i,pos_col,"-"*(scacchiera.c*4))
        
    for i in range(0,scacchiera.c*4+1,4):
        for j in range(0,scacchiera.r*4+1,1):
            screen.addstr(pos_rig+j,pos_col+i,"|")

    for i in range(0,scacchiera.r*4+1,4):
        for j in range(0,scacchiera.c*4+1,4):
            screen.addstr(pos_rig+i,pos_col+j,"+")   
        
    for righe in range(1,scacchiera.r+1):
        screen.addstr(pos_rig+2+4*(righe-1), pos_col-1,  str(righe))
        
    for colonne in range(1, scacchiera.c+1):
        screen.addstr(pos_rig-1, pos_col+2+4*(colonne-1), str(colonne))

    if isinstance(scacchiera, ScacchieraNavi):
        StampaNavi(scacchiera, screen, pos_rig, pos_col)
        StampaColpito(scacchiera, screen, pos_rig, pos_col)
    else:
        StampaColpi(scacchiera, screen, pos_rig, pos_col)
     
     

def StampaSimboli(scacchiera, screen, pos_rig, pos_col, simbolo):
    for posizione in scacchiera.posizioni:
        screen.addstr((pos_rig+2)+4*(posizione[0]-1),(pos_col+2)+4*(posizione[1]-1),simbolo)


def StampaNavi(scacchiera, screen, pos_rig, pos_col):
    StampaSimboli(scacchiera, screen, pos_rig, pos_col, 'x')

def StampaColpi(scacchiera, screen, pos_rig, pos_col):
    StampaSimboli(scacchiera, screen, pos_rig, pos_col, 'o')

def StampaColpito(scacchiera, screen, pos_rig, pos_col):
    for posizione in scacchiera.navi_abbattute:
        screen.addstr((pos_rig+2)+4*(posizione[0]-1),(pos_col+2)+4*(posizione[1]-1),'#')

    
