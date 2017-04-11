from scacchiera_nc import *
import curses

screen=curses.initscr()

curses.curs_set(0)

#Giocatore1

scacchiera1=ScacchieraNC(screen, 5, 5, 5, 5)

scacchiera1.posizione_nave((4,4), 2, 'h')
scacchiera1.posizione_nave((1,1), 2, 'v')
scacchiera1.posizione_nave((1,1), 2, 'h')
scacchiera1.posizione_nave((4,2), 2, 'h')

scacchiera1.stampa()
#scacchiera2.stampa()
scacchiera1.stampa_navi()

#scacchiera2=ScacchieraNC(screen, 5, 5, 5, 40)

#Giocatore2

#scacchiera3=ScacchieraNC(screen, 5, 5, 5, 70)
#scacchiera4=ScacchieraNC(screen, 5, 5, 5, 95)
#scacchiera3.stampa()
#scacchiera4.stampa()

screen.refresh()

screen.getch()

curses.endwin()
