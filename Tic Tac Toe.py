
import time
import random
from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("Tic Tac Toe")

wind_width = 520
wind_height = 535
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coord  = (screen_width/2)-(wind_width/2)
y_coord  = (screen_height/2)-(wind_height/2)
root.geometry("%dx%d+%d+%d" % (wind_width, wind_height, x_coord, y_coord))

root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(1, weight = 1)
root.grid_columnconfigure(2, weight = 1)
root.grid_rowconfigure(0, weight = 1)
root.grid_rowconfigure(1, weight = 1)
root.grid_rowconfigure(2, weight = 1)
root.grid_rowconfigure(3, weight = 1)


grid_list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
winner = False
winner_stat = ""
player_turn = True
score = {"X": 0, "O": 0}
score_text = "X: {} | O: {}".format(score["X"], score["O"])

#colour lists: root, button bg, button fg
defaultcol = ["#D4163B", "#A51184", "#400032"]
greens = ["#056347", "#019B6C", "#00291D"]
orange = ["#972A08", "#EB3A02", "#3E0F00"]
blue = ["#015B8B", "#049FF3", "#001825"]
yellow = ["#C5A500", "#FFD600", "#2A2300"]
red = ["#9B0000", "#FF0000", "#2A0000"]

all_colours = [greens, defaultcol, yellow, orange, red, blue]

grid_relief = "sunken"
button_height = 1
button_width = 3
button_bg = defaultcol[1]
button_fg = defaultcol[2]
root_colour = defaultcol[0]
grid_font = "Verdana 50 bold"
top_font = "Verdana 12 bold"
score_font = "Verdana 13 bold"

root.configure(bg = root_colour)


cycle = Button(root, text = "Cycle Colours", fg = button_fg, bg = button_bg, font = top_font, command = lambda: Cycle())
cycle.grid(row = 0, column = 0)

scoreboard = Label(root, text = score_text, bd = 4, relief = "ridge", fg = button_fg, bg = button_bg, font = score_font, padx = 12, pady = 5)
scoreboard.grid(row = 0, column = 1)

restart = Button(root, text = "Restart Game", fg = button_fg, bg = button_bg, font = top_font, command = lambda: play_again())
restart.grid(row = 0, column = 2)


def Cycle():
    global button_bg, button_fg, root_colour, all_colours
    root_colour = all_colours[0][0]
    button_bg = all_colours[0][1]
    button_fg = all_colours[0][2]
    root.configure(bg = root_colour)
    for x in all_widgets:
        x.configure(bg = button_bg, fg = button_fg)
    all_colours.insert(0, all_colours.pop(-1))


def endgame():
    global winner_stat
    endgame = tkinter.messagebox.askquestion("Game Over" , winner_stat + "\nWould you like to play again?")
    if endgame == "yes":
        play_again()
    if endgame == "no":
        close_window()


def play_again():
    global grid_list
    global winner
    global winner_stat
    grid_list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    winner = False
    winner_stat = ""
    upd_grid()


def close_window():
    root.destroy()


def Add_X(button, x):
    global player_turn
    global grid_list
    if player_turn == True:
        if grid_list[x] == " " and winner == False:
            grid_list[x] = "X"
            button.configure(text = grid_list[x])
        player_turn = False
    print(grid_list)
    upd_grid()
    check_state("X")


def Add_O():
    root.after(200)
    global player_turn
    global grid_list
    if player_turn == False:
        if " " in grid_list and winner == False:
            empty = [i for i, x in enumerate(grid_list) if x == " "]
            select = random.choice(empty)
            grid_list[select] = "O"
            player_turn = True
    upd_grid()
    check_state("O")


def Combine(button, x):
    if grid_list[x] == " ":
        Add_X(button, x)
        Add_O()


def upd_grid():
    button1["text"] = grid_list[0]
    button2["text"] = grid_list[1]
    button3["text"] = grid_list[2]
    button4["text"] = grid_list[3]
    button5["text"] = grid_list[4]
    button6["text"] = grid_list[5]
    button7["text"] = grid_list[6]
    button8["text"] = grid_list[7]
    button9["text"] = grid_list[8]
    scoreboard["text"] = score_text


def check_state(c):
    global grid_list, winner, winner_stat, score, score_text
    a = c *3
    if "".join(grid_list[0:3]) == a\
            or "".join(grid_list[3:6]) == a\
            or "".join(grid_list[6:9]) == a\
            or "".join(grid_list[0:9:3]) == a \
            or "".join(grid_list[1:9:3]) == a \
            or "".join(grid_list[2:9:3]) == a \
            or "".join(grid_list[0:9:4]) == a \
            or "".join(grid_list[2:7:2]) == a\
            and winner == False:
        print(c + " Wins!")
        winner_stat = "Player %s is the Winner!" %c
        winner = True
        score[c] += 1
        score_text = "X: {} | O: {}".format(score["X"], score["O"])
        endgame()
    if " " not in grid_list and winner == False:
        print("It's a draw")
        winner_stat = "It's a draw!"
        winner = False
        endgame()


button1 = Button(root, text= grid_list[0], relief = grid_relief, fg = button_fg, bg = button_bg, font = grid_font, height = button_height, width = button_width, command = lambda: Combine(button1, 0))
button1.grid(row = 1, column = 0)
button1.bind("<Button-1>")

button2 = Button(root, text= grid_list[1], relief = grid_relief, fg = button_fg, bg = button_bg, font = grid_font, height = button_height, width = button_width, command = lambda: Combine(button2, 1))
button2.grid(row = 1, column = 1)
button2.bind("<Button-1>")

button3 = Button(root, text= grid_list[2], relief = grid_relief, fg = button_fg, bg = button_bg, font = grid_font, height = button_height, width = button_width, command = lambda: Combine(button3, 2))
button3.grid(row = 1, column = 2)
button3.bind("<Button-1>")

button4 = Button(root, text= grid_list[3], relief = grid_relief, fg = button_fg, bg = button_bg, font = grid_font, height = button_height, width = button_width, command = lambda: Combine(button4, 3))
button4.grid(row = 2, column = 0)
button4.bind("<Button-1>")

button5 = Button(root, text= grid_list[4], relief = grid_relief, fg = button_fg, bg = button_bg, font = grid_font, height = button_height, width = button_width, command = lambda: Combine(button5, 4))
button5.grid(row = 2, column = 1)
button5.bind("<Button-1>")

button6 = Button(root, text= grid_list[5], relief = grid_relief, fg = button_fg, bg = button_bg, font = grid_font, height = button_height, width = button_width, command = lambda: Combine(button6, 5))
button6.grid(row = 2, column = 2)
button6.bind("<Button-1>")

button7 = Button(root, text= grid_list[6], relief = grid_relief, fg = button_fg, bg = button_bg, font = grid_font, height = button_height, width = button_width, command = lambda: Combine(button7, 6))
button7.grid(row = 3, column = 0)
button7.bind("<Button-1>")

button8 = Button(root, text= grid_list[7], relief = grid_relief, fg = button_fg, bg = button_bg, font = grid_font, height = button_height, width = button_width, command = lambda: Combine(button8, 7))
button8.grid(row = 3, column = 1)
button8.bind("<Button-1>")

button9 = Button(root, text= grid_list[8], relief = grid_relief, fg = button_fg, bg = button_bg, font = grid_font, height = button_height, width = button_width, command = lambda: Combine(button9, 8))
button9.grid(row = 3, column = 2)
button9.bind("<Button-1>")

all_widgets = (button1, button2, button3, button4, button5, button6, button7, button8, button9, cycle, scoreboard, restart)

'''
UserInfo = Entry(root)
UserInfo.grid(row = 0, column = 1)
'''
#root.after_idle(0, Add_O(None))
#root.after_idle(Add_O, None)

#root.bind("<KeyPress-H>", cock())
#if player_turn == False:
#    root.event_generate("<KeyPress-H>", when = "tail")


root.mainloop()
