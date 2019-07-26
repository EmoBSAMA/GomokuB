#初始化加载
version="0.0.1"     #版本号
board = [[0 for i in range(15)] for j in range(15)]     #内棋盘加载
boardsh=[["  " for i in range(15)] for j in range(15)]     #外棋盘加载
a=""
again=""
x=0
y=0

'''
borad[x][y]  采用坐标轴形式表示
0=null，1=1P，2=2P

'''

#调用其他文件函数
from AIChoose import *
from Boardupdate import *
from Judge import *


def boardcleaner(): #棋盘清理函数
    global boardsh,boardshow,x,y
    while x<15:
        while y<15:
            board[x][y]=0
            boardsh[x][y]="  "
            y+=1
        y=0
        x+=1
    x=0

def boardshow():    #外棋盘变更与展示函数
    global boardsh,boardshow,x,y
    #外棋盘变更


    
    #外棋盘展示
    print("    1   2   3   4   5   6   7   8   9   10  11  12  13  14  15")
    print("  ┌─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┐")
    for y in range(15):
        if y<9:
            print(" "+str(y+1),sep="",end="")
        else:
            print(y+1,sep="",end="")
        for x in range(15):
            print("│"+str(boardsh[x][y]),sep="",end="")
        print("│")
        if y<14:
            print("  ├─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┤")
        else:
            print("  └─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┘")

    
'''
    print("   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15")
    print(" ┌─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┐")
    print("1│○│○│○│○│○│○│○│○│○│○│○│○│○│○│○│")
    print(" ├─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┤")
    print("2│○│○│○│○│○│○│○│○│○│○│○│○│○│○│○│")
'''

def boardchange():  #玩家选择与内棋盘变更函数
    global boardsh,x,y

'''
-----------------------------------------------------
各函数与变量会在此处显示和解释
AIChoose

Boardupdate

Judge


-----------------------------------------------------
'''

#开始界面
print("-----------------------------------------------------\n欢迎来到GomokuB\n\n\n制作者EmoBSAMA")
print("版本号："+version+"\n\n\n")
print("目前只可以选择双人模式，按回车键可开始游戏")
a=input()

#游戏界面
boardcleaner()
boardshow()
#结束界面
print("感谢您的游玩，需要再来一次请输入 y ")
again=input()



