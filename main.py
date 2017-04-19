from scacchiera_nc import *
from scacchiera_navi import *
from scacchiera_colpi import *
import curses

screen=curses.initscr()

curses.curs_set(0)

#Giocatore1

scacchiera1=ScacchieraNavi(5, 5)

scacchiera1.posizione_nave((4,4), 2, 'h')
scacchiera1.posizione_nave((1,1), 2, 'v')
scacchiera1.posizione_nave((1,1), 2, 'h')
scacchiera1.posizione_nave((4,2), 2, 'h')

StampaScacchiera(scacchiera1, screen, 5, 5)

scacchiera2=ScacchieraColpi(5, 5)

scacchiera2.posizione_colpi((4,3))

StampaScacchiera(scacchiera2, screen, 5, 40) 

#Giocatore2

#scacchiera3=ScacchieraNavi(5, 5)
#StampaScacchiera(scacchiera3, screen, 5, 70)
#scacchiera4=ScacchieraNavi(5, 5)
#StampaScacchiera(scacchiera4, screen, 5, 95)

screen.refresh()

screen.getch()

curses.endwin()
