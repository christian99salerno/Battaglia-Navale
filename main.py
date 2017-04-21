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

scacchiera1=ScacchieraNavi(5, 5)

scacchiera1.posizione_nave((4,4), 2, 'h')
scacchiera1.posizione_nave((1,1), 2, 'v')

scacchiera2=ScacchieraColpi(5, 5)



#Giocatore2

scacchiera3=ScacchieraColpi(5, 5)

scacchiera4=ScacchieraNavi(5, 5)

scacchiera4.posizione_nave((4,3), 1, "h")
scacchiera4.posizione_nave((2,2), 2, "h")
#scacchiera4.BreakShip((4,3))
#scacchiera2.posizione_colpi((4,3))
#scacchiera4.BreakShip((2,3))
#scacchiera2.posizione_colpi((2,3))
legami(scacchiera2, scacchiera4, (4,3))

StampaScacchiera(scacchiera1, screen, 5, 5)
StampaScacchiera(scacchiera4, screen, 5, 160)

StampaScacchiera(scacchiera2, screen, 5, 30) 
StampaScacchiera(scacchiera3, screen, 5, 135)

screen.refresh()

screen.getch()

curses.endwin()
