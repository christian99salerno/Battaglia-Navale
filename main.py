from scacchiera_nc import *
import curses

screen=curses.initscr()

curses.curs_set(0)

scacchiera1=ScacchieraNC(screen, 5, 5, 5, 5)
scacchiera1.posizione_nave((3,2))

#scacchiera2=ScacchieraNC(screen, 5, 5)

#scacchiera3=ScacchieraNC(screen, 5, 5)
#scacchiera4=ScacchieraNC(screen, 5, 5)

#Giocatore1
scacchiera1.stampa()
scacchiera1.stampa_navi()
#scacchiera2.stampa(5, 40)


#Giocatore2
#scacchiera3.stampa(5, 70)
#scacchiera4.stampa(5, 95)

screen.refresh()

screen.getch()

curses.endwin()
