from CSP import *
import sys
import curses
import click
import time

if __name__ == "__main__":
    BTStr = ["-backtracking","-BackTracking","-bt","BT"]
    BJStr = ["-backjumping","-BackJumping","-bj","BJ"]
    EvilStr = ["-Evil","-evil"]
    EasyStr = ["-Easy","-easy"]
    # check the parameters
    if len(sys.argv) != 3 or not sys.argv[1] in BTStr+BJStr or not sys.argv[2] in EvilStr+EasyStr :
        print("Ussage: python3 Test.py [Algorithm] [PuzzleType]")
        print("Choice of algorithms:")
        print("\t 1.'-backtracking', '-BackTracking', '-bt', '-BT': Backtracking")
        print("\t 2.'-backjumping', '-BackJumping', '-bj', '-bj': Conflict-directed Backjumping")
        print("Choice of puzzle types:")
        print("\t 1.'-Easy', '-easy': Easy puzzle")
        print("\t 2.'-Evil', '-evil': Evil puzzle")
        print("e.g. python3 Test.py -backtracking -easy ")
        exit()
    # Run the algorithm accordingly
    start = time.time()
    if sys.argv[1] in BJStr :
        if sys.argv[2] in EvilStr :
            BackJumpingSearch(PuzzleType.evil)
        else :
            BackJumpingSearch(PuzzleType.easy)
    else :
        if sys.argv[2] in EvilStr :
            BacktrackingSearch(PuzzleType.evil)
        else :
            BacktrackingSearch(PuzzleType.easy)
    end = time.time()
    print("\n\r[done]\r")
    print("[Total time: %s s]\r\n"%(end-start))
    # Wait for user input to end
    curses.nocbreak()
    curses.initscr().keypad(False)
    curses.echo()
    print("Press any key to end ...\n\r")
    if click.getchar():
        curses.endwin()

