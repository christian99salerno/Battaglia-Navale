from scacchiera_nc import *
import curses

screen=curses.initscr()

curses.curs_set(0)

scacchiera1=ScacchieraNC(screen, 5, 5)

scacchiera1.stampa(5, 5)

screen.refresh()

screen.getch()

curses.endwin()
