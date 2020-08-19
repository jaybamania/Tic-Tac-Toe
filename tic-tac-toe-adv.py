from tkinter import *
import tkinter.messagebox as tm
from tkinter.ttk import Progressbar

p1,p2 = 'Player1' , 'Player2'
Z=0
sX, sO = 0,0
player = 'X'

def playAgain():
    global stop_game
    stop_game = False
    onButtons()
    for i in range(3):
        for j in range(3):
            states[i][j]=0
            b[i][j].config(text='',bg='powder blue')

def score():
    global player, Z, sX, sO,root
    won = Z
    nextPlay.config(state=DISABLED)
    if won == 'X':
        sX += 1
        scoreX.config(text="{}[X]: {}".format(p1,sX))
    elif won == 'O':
        sO += 1
        scoreO.config(text="{}[O]: {}".format(p2,sO))

    if sX == 3 or sO == 3:
        stop_game = TRUE
        winner = tm.askyesno("Game Over","Highest Score:\n\t{}\n\t{}\nDo you want to play again?".format(scoreX.cget('text'),scoreO.cget('text')))
        if winner == TRUE:
            playAgain()
            sX,sO = 0,0
            scoreX.config(text="{}[X]: {}".format(p1,sX))
            scoreO.config(text="{}[O]: {}".format(p2, sO))
        elif winner == FALSE:
            exiting = tm.showinfo("Come Soon","Hope You Enjoyed the game.\nGame is Exiting...")
            root.destroy()

def offButtons():
    for i in range(3):
        for j in range(3):
            b[i][j].config(state=DISABLED)

def onButtons():
    for i in range(3):
        for j in range(3):
            b[i][j].config(state=NORMAL)

def  getName():
    global player,p1,p2,player1E,player2E
    p1 = player1E.get()
    p2 = player2E.get()
    print("Player1: ",p1," Player2: ",p2)
    scoreX.config(text="{}[X]: 0".format(p1))
    scoreO.config(text="{}[O]: 0".format(p2))
    root.deiconify()
    mainWindow.destroy()
i=0
loadingLabel=0
progress=0

def load():
    global i,progress,loadingLabel
    loadingLabel = Label(mainWindow,text="",font=('arial',10,'bold'),fg='blue')
    loadingLabel.place(x=400,y=420)
    progress = Progressbar(mainWindow,orient=HORIZONTAL,length=250,mode='determinate')
    progress.place(x=150,y=420)
    if i<=10:
        txt = str(10*i)+'%'
        loadingLabel.config(text=txt)
        loadingLabel.after(1000,load)
        progress['value'] = int(10*i)
        i += 1
    if progress['value'] == 100:
        getName()

def mode2():
    global player1E,player2E
    mode.destroy()
    singleMode.destroy()
    twoMode.destroy()
    player1 = Label(mainWindow,text="Player 1 Name : ",bg='red',font=('arial',10),fg='white')
    player1.place(x=200,y=330)
    player1E = Entry(mainWindow,fg='blue',highlightbackground='blue',highlightthickness=2,width=30)
    player1E.place(x=310,y=330)

    player2 = Label(mainWindow, text="Player 2 Name : ", bg='red', font=('arial', 10), fg='white')
    player2.place(x=200, y=360)
    player2E = Entry(mainWindow, fg='blue', highlightbackground='blue', highlightthickness=2, width=30)
    player2E.place(x=310, y=360)

    submit=Button(mainWindow,text="Play game",bg='blue',fg='white',width=15,command=load)
    submit.place(x=280,y=390)

def exitWindows(e):
    try:
        mainWindow.wm_attributes('-topmost',FALSE)
        msg = tm.askyesno(title="Exit Game",message='Do you really want to exit Game?')
    except:
        msg = tm.askyesno(title="Exit Game", message='Do you really want to exit Game?')
    if msg ==TRUE:
        sys.exit(root.destroy())

def callback(r,c):
    global player
    if player=='X' and states[r][c]==0 and stop_game ==FALSE:
        b[r][c].config(text='X',fg='blue',bg='white')
        states[r][c] = 'X'
        player = 'O'
    if player=='O' and states[r][c]==0 and stop_game ==FALSE:
        b[r][c].config(text='O',fg='orange',bg='black')
        states[r][c] = 'O'
        player = 'X'
    check_winner()

def check_winner():
    global stop_game,Z

    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] != 0:
            b[i][0].config(bg='grey')
            b[i][1].config(bg='grey')
            b[i][2].config(bg='grey')
            stop_game=TRUE
            Z = states[i][0]

            winner = tm.showinfo("Winner",states[i][0]+' Won!')
            offButtons()
            score()
            break

        elif states[0][i] == states[1][i] == states[2][i] != 0:
            b[0][i].config(bg='grey')
            b[1][i].config(bg='grey')
            b[2][i].config(bg='grey')
            stop_game = TRUE
            Z = states[0][i]

            winner = tm.showinfo("Winner", states[0][i] + ' Won!')
            offButtons()
            score()
            break

        if states[0][0] == states[1][1] == states[2][2] != 0:
            b[0][0].config(bg='grey')
            b[1][1].config(bg='grey')
            b[2][2].config(bg='grey')
            stop_game = TRUE
            Z = states[0][0]

            winner = tm.showinfo("Winner", states[1][1] + ' Won!')
            offButtons()
            score()
            break

        if states[2][0] == states[1][1] == states[0][2] != 0:
            b[0][2].config(bg='grey')
            b[1][1].config(bg='grey')
            b[2][0].config(bg='grey')
            stop_game = TRUE
            Z = states[2][0]

            winner = tm.showinfo("Winner", states[1][1] + ' Won!')
            offButtons()
            score()
            break

    nextPlay.config(text="Play Again",bg="red",state=NORMAL)

root = Tk()
root.title('TIC TAC TOE')
root.resizable(0,0)

root.tk.call('wm','iconphoto',root._w, PhotoImage(file='ttt.png'))
root.bind('<Escape>',exitWindows)
bg = PhotoImage(file="ttt.png")
bgImage = Label(root, image=bg).place(x=-60,y=0)

b=[[0,0,0],
   [0, 0, 0],
   [0, 0, 0]]

states =[[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(3):
    for j in range(3):
        b[i][j] = Button(font=('Verdana',60), width=3, bg='powder blue', command=lambda r=i,c=j:callback(r,c))
        b[i][j].grid(row=i,column=j)

mainWindow= Toplevel(root)
mainWindow.title("Play TIC TAC TOE - Home")
mainWindow.wm_iconbitmap("tic-tac-toe.ico")
mainWindow.overrideredirect(1)
mainWindow.config(bg='green')
mainWindow.bind('<Escape>',exitWindows)

height = 450
width = 580
x = (root.winfo_screenwidth()//2) -(width//2)
y = (root.winfo_screenheight()//2) - (height//2)
mainWindow.geometry("{}x{}+{}+{}".format(width,height,x,y))
mainWindow.wm_attributes('-topmost',True)

bgImage = Label(mainWindow, image=bg).place(x=-30,y=0)

devBy = Label(mainWindow,text="TIC TAC TOE",font=('mistral',10,'bold'),fg='blue',bg='powder blue',width=150)
devBy.pack(side=TOP)

mode = Label(mainWindow,text="CHOOSE MODE",bg='blue',fg='goldenrod1',font=('impact',12),width=20)
mode.place(x=180,y=220)

def onButtonS(e):
    singleMode['bg'] = 'goldenrod3'

def leaveButtonS(e):
    singleMode['bg'] = 'goldenrod1'

def onButtonT(e):
    twoMode['bg'] = 'goldenrod3'
def leaveButtonT(e):
    twoMode['bg'] = 'goldenrod1'

singleMode = Button(mainWindow,text="Single Player",bg='goldenrod1',width=20,activebackground='goldenrod3',activeforeground='blue')
singleMode.place(x=190,y=250)
singleMode.bind('<Enter>',onButtonS)
singleMode.bind('<Leave>',leaveButtonS)

twoMode = Button(mainWindow,text="Two Player",bg='goldenrod1',width=20,activebackground='goldenrod3',activeforeground='blue',command=mode2)
twoMode.place(x=190,y=280)
twoMode.bind('<Enter>',onButtonT)
twoMode.bind('<Leave>',leaveButtonT)

nextPlay = Button(root,text="",width=10,bd=0,command=playAgain)
nextPlay.grid(row=4,column=1)

scoreX = Label(root, text="Score X: ",font=('mistral',12))
scoreX.grid(row=4,column=0)

scoreO = Label(root, text="Score O: ",font=('mistral',12))
scoreO.grid(row=4,column=2)
stop_game = FALSE

copyrigh = Label(root, text="Developed By JayBamania",font=('mistral',12,'bold'),fg='blue',bg='powder blue',width=70)
copyrigh.grid(row=5,columnspan=3)

root.withdraw()
mainloop()