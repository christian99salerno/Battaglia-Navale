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

screen.addstr(1,5,"Giocatore:1")

scacchiera1=ScacchieraNavi(5, 5)

scacchiera1.posizione_nave((4,4), 2, 'h')
scacchiera1.posizione_nave((1,1), 2, 'v')
scacchiera1.posizione_nave((1,3), 1, "v")
scacchiera1.posizione_nave((5,1), 1, 'v')
scacchiera1.posizione_nave((2,5), 1, 'v')

scacchiera2=ScacchieraColpi(5, 5)



#Giocatore2

screen.addstr(1,140,"Giocatore:2")

scacchiera3=ScacchieraColpi(5, 5)

scacchiera4=ScacchieraNavi(5, 5)

scacchiera4.posizione_nave((4,3), 1, "h")
scacchiera4.posizione_nave((2,2), 2, "h")

legami(scacchiera2, scacchiera4, (4,3))
legami(scacchiera3, scacchiera1, (2,2))
legami(scacchiera3, scacchiera1, (1,1))
legami(scacchiera3, scacchiera1, (2,1))
legami(scacchiera3, scacchiera1, (1,3))
legami(scacchiera3, scacchiera1, (2,5))
legami(scacchiera3, scacchiera1, (4,4))
legami(scacchiera3, scacchiera1, (4,5))
legami(scacchiera3, scacchiera1, (5,1))

StampaScacchiera(scacchiera1, screen, 5, 5)
StampaScacchiera(scacchiera4, screen, 5, 165)

StampaScacchiera(scacchiera2, screen, 5, 30) 
StampaScacchiera(scacchiera3, screen, 5, 140)

screen.refresh()

screen.getch()

curses.endwin()
