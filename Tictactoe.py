def drawtable(t):
    for i in t:
        print (i)
def selectsquare1(a,t):
    while not a in ["11","12","13","21","22","23","31","32","33"]:
        a=input('please select a viable format (viable formats are:"11","12","13","21","22","23","31","32","33"): ')
    i=int(a[0])-1
    j=int(a[1])-1
    while not t[i][j]==' ':
        a=input('this square is full please select an empty square: ')
        i=int(a[0])-1
        j=int(a[1])-1
    t[i][j]='X'
def selectsquare2(a,t):
    while not a in ["11","12","13","21","22","23","31","32","33"]:
        a=input('please select a viable format (viable formats are:"11","12","13","21","22","23","31","32","33"): ')
    i=int(a[0])-1
    j=int(a[1])-1
    while not t[i][j]==' ':
        a=input('this square is full please select an empty square: ')
        i=int(a[0])-1
        j=int(a[1])-1
    t[i][j]='O'
def checkdraw(t):
    for i in t:
        for j in i:
            if j==' ':
                return True
    return False
t=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
M=True
while True:
    drawtable(t)
    Player_1=input('Player 1 select square:')
    selectsquare1(Player_1,t)
    drawtable(t)
    if t[0]==['X','X','X'] or t[1]==['X','X','X'] or t[2]==['X','X','X'] or (t[0][0]=='X' and t[1][1]=='X' and t[2][2]=='X') or (t[0][2]=='X' and t[1][1]=='X' and t[2][0]=='X') or (t[0][0]=='X' and t[0][1]=='X' and t[0][2]=='X') or (t[1][0]=='X' and t[1][1]=='X' and t[1][2]=='X') or (t[2][0]=='X' and t[2][1]=='X' and t[2][2]=='X'):
        print("player 1 won!!!!!!!!!!!!!! better luck for player 2 next time")
        break
    M=checkdraw(t)
    if not M:
        print("Draw try next time")
        break
    Player_2=input("Player 2 select square:")
    selectsquare2(Player_2,t)
    drawtable(t)
    if t[0]==["O","O","O"] or t[1]==["O","O","O"] or t[2]==["O","O","O"] or (t[0][0]=="O" and t[1][1]=="O" and t[2][2]=="O") or (t[0][2]=="O" and t[1][1]=="O" and t[2][0]=="O") or (t[0][0]=="O" and t[0][1]=="O" and t[0][2]=="O") or (t[1][0]=="O" and t[1][1]=="O" and t[1][2]=="O") or (t[2][0]=="O" and t[2][1]=="O" and t[2][2]=="O"):
        print("player 2 won!!!!!!!!!!!!!! You totally outplayed Player_1")
        break

