from scacchiera_nc import *
import curses

screen=curses.initscr()

curses.curs_set(0)

scacchiera1=ScacchieraNC(5, 5)

scacchiera1.stampa(screen, 5, 5)

screen.refresh()

screen.getch()

curses.endwin()
