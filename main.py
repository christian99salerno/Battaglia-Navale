from scacchiera_nc import *
import curses

screen=curses.initscr()

curses.curs_set(0)

scacchiera1=ScacchieraNC(screen, 5, 5)
scacchiera2=ScacchieraNC(screen, 5, 5)

scacchiera3=ScacchieraNC(screen, 5, 5)
scacchiera4=ScacchieraNC(screen, 5, 5)

#Giocatore1
scacchiera1.stampa(5, 5)
scacchiera2.stampa(5, 30)

#Giocatore2
scacchiera3.stampa(5, 65)
scacchiera4.stampa(5, 90)

screen.refresh()

screen.getch()

curses.endwin()
