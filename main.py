from scacchiera_nc import *
from scacchiera_navi import *
from scacchiera_colpi import *
import curses

def legami(scacchiera1, scacchiera2, coordinata):
    scacchiera1.posizione_colpi(coordinata)
    scacchiera2.BreakShip(coordinata)


screen=curses.initscr()

curses.curs_set(0)

#Giocatore1

screen.addstr(1,5,"Player:1")
screen.addstr(28, 5, "Inserisci:")
screen.addstr(1,140,"Player:2")
screen.addstr(28, 140, "Inserisci:")

scacchiera1=ScacchieraNavi(5, 5)
scacchiera2=ScacchieraColpi(5, 5)
scacchiera3=ScacchieraColpi(5, 5)
scacchiera4=ScacchieraNavi(5, 5)

StampaScacchiera(scacchiera1, screen, 5, 5)
StampaScacchiera(scacchiera2, screen, 5, 30) 
StampaScacchiera(scacchiera3, screen, 5, 140)
StampaScacchiera(scacchiera4, screen, 5, 165)

while scacchiera1.navi1max>0 or scacchiera1.navi2max>0:
   

    screen.addstr(30, 5, "Navi da uno:"+str(scacchiera1.navi1max))
    screen.addstr(31, 5, "Navi da due:"+str(scacchiera1.navi2max))
 
    screen.addstr(33, 5, '1/2?              ')
    tipo_nave = int(screen.getstr(33, 10, 2))

    if tipo_nave==1:
        screen.addstr(35, 5, 'Riga?')
        r = int(screen.getstr(35, 11, 2))
        screen.addstr(36, 5, 'Colonna?')
        c = int(screen.getstr(36, 14, 2))
        scacchiera1.posizione_nave((r,c), 1, "v")
    elif tipo_nave==2:
        screen.addstr(35, 5, 'Riga?')
        r = int(screen.getstr(35, 11, 2))
        screen.addstr(36, 5, 'Colonna?')
        c = int(screen.getstr(36, 14, 2))
        screen.addstr(37, 5, 'Verso?')
        verso = screen.getstr(37, 12, 2)
        scacchiera1.posizione_nave((r,c), 2, verso)
    
    StampaScacchiera(scacchiera1, screen, 5, 5)
    StampaScacchiera(scacchiera2, screen, 5, 30) 
    StampaScacchiera(scacchiera3, screen, 5, 140)
    StampaScacchiera(scacchiera4, screen, 5, 165)
    screen.addstr(35, 0, "\n\n\n\n\n\n\n\n\n\n")

screen.addstr(29, 140, "\n\n\n\n\n\n\n\n\n\n")

while scacchiera4.navi1max>0 or scacchiera4.navi2max>0:
    

    screen.addstr(30, 140, "Navi da uno:"+str(scacchiera4.navi1max))
    screen.addstr(31, 140, "Navi da due:"+str(scacchiera4.navi2max))
 
    screen.addstr(33, 140, '1/2?              ')
    tipo_nave = int(screen.getstr(33, 145, 2))

    if tipo_nave==1:
        screen.addstr(35, 140, 'Riga?')
        r = int(screen.getstr(35, 146, 2))
        screen.addstr(36, 140, 'Colonna?')
        c = int(screen.getstr(36, 149, 2))
        scacchiera4.posizione_nave((r,c), 1, "v")
    elif tipo_nave==2:
        screen.addstr(35, 140, 'Riga?')
        r = int(screen.getstr(35, 146, 2))
        screen.addstr(36, 140, 'Colonna?')
        c = int(screen.getstr(36, 149, 2))
        screen.addstr(37, 140, 'Verso?')
        verso = screen.getstr(37, 147, 2)
        scacchiera4.posizione_nave((r,c), 2, verso)
   
    StampaScacchiera(scacchiera1, screen, 5, 5)
    StampaScacchiera(scacchiera2, screen, 5, 30) 
    StampaScacchiera(scacchiera3, screen, 5, 140)
    StampaScacchiera(scacchiera4, screen, 5, 165)
    screen.addstr(35, 140, "\n\n\n\n\n\n\n\n\n\n")

screen.addstr(29, 140, "\n\n\n\n\n\n\n\n\n\n")

while scacchiera1.cbreak<ScacchieraNavi.maxnavi and scacchiera4.cbreak<ScacchieraNavi.maxnavi:
    
    screen.addstr(30, 5, 'Riga?')
    r = int(screen.getstr(30, 11, 2))
    screen.addstr(31, 5, 'Colonna?')
    c = int(screen.getstr(31, 14, 2))
    legami(scacchiera2,scacchiera4,(r,c))
    screen.addstr(30, 0, "\n\n\n\n\n\n\n\n\n\n")
    
    StampaScacchiera(scacchiera1, screen, 5, 5)
    StampaScacchiera(scacchiera2, screen, 5, 30) 
    StampaScacchiera(scacchiera3, screen, 5, 140)
    StampaScacchiera(scacchiera4, screen, 5, 165)
    
    if scacchiera4.cbreak < ScacchieraNavi.maxnavi:
        screen.addstr(30, 140, 'Riga?')
        r = int(screen.getstr(30, 146, 2))
        screen.addstr(31, 140, 'Colonna?')
        c = int(screen.getstr(31, 149, 2))
        legami(scacchiera3,scacchiera1,(r,c))
        screen.addstr(30, 140, "\n\n\n\n\n\n\n\n\n")
    
        StampaScacchiera(scacchiera1, screen, 5, 5)
        StampaScacchiera(scacchiera2, screen, 5, 30) 
        StampaScacchiera(scacchiera3, screen, 5, 140)
        StampaScacchiera(scacchiera4, screen, 5, 165)

screen.addstr(15, 88, 'Game Over')

if scacchiera1.cbreak==7:
   screen.addstr(16, 82, 'The Winner is Player2')
else:
   screen.addstr(16, 82, 'The Winner is Player1')

screen.refresh()

screen.getch()

curses.endwin()
