import copy
import random
class test:
    def __init__(self):
        self.width = 20
        self.height = 20
pp = test()
MAX_BOARD = 20
board = [[0 for i in range(MAX_BOARD)] for j in range(MAX_BOARD)]
# board[10][10] = 2
# board[10][9]=2
# board[3][5]=2

import copy
N = 3
score = [0, 1000, -1000]
import util as ut
ut.pp.width = pp.width
ut.pp.height = pp.height
min_or_max = ["max", "min"]
from Node import Node
from Node import KillDict
import hash
StateDict = {}
IsExistKill = 0
global_hashtable = hash.hash(pp.width, pp.height)



def boardtolist(board):
    change = []
    for a in range(pp.width):
        for b in range(pp.height):
            if board[a][b] > 0:
                change.append((a,b,board[a][b]))
    return tuple(change)



def brain_turn():
    # if pp.terminateAI:
    #     return
    global IsExistKill
    alpha = float('-inf')
    beta = float('inf')
    boardtemp = copy.deepcopy([a[0:pp.width] for a in board[0:pp.height]])
    if IsExistKill == 1: # 若存在连续杀棋则从字典里找要下哪步，若该点不在字典里则说明对方没有堵
       li = boardtolist(boardtemp)
       print('hrer')
       if li in KillDict:
           nextcd = KillDict[li]
           return nextcd
       else:
           root = Node(next_cd=(-1, -1), who=2, boardNow=boardtemp)
           rtnode = get_value(root, alpha, beta, 0)
           return rtnode.next_cd

    root = Node(next_cd=(-1, -1), who=2, boardNow=boardtemp)## 寻找杀棋
    rtnode = root.check_kill_chess(1)
    if (rtnode.value) == 100:
        # IsExistKill = 1
        print('find')
        print(rtnode.next_cd)
        return rtnode.next_cd

    oproot = Node(next_cd=(-1, -1), who=1, boardNow=boardtemp)## 寻找对面杀棋，若有则堵
    opnode = oproot.check_kill_chess(2, 2)
    if (opnode.value == 100):
        print('op has kill')
        print(opnode.next_cd)
        return opnode.next_cd
        # print(KillDict)

    root = Node(next_cd=(-1,-1), who=2, boardNow=boardtemp) ## 正常下棋
    rtnode = get_value(root, alpha, beta, 0)
    print(rtnode.next_cd, rtnode.value)

    return rtnode.next_cd

def get_value(node, alpha, beta, iteration):

    # t = boardtolist(node.board)
    # if t in StateDict:
    #     node.value = StateDict[t]
    #     # print("have explored")
    #     return node

    # end = ut.check_success(node.board, node.next_cd[0], node.next_cd[1], who=node.who)
    end = ut.ck_success(node)
    if (end)>=0:
        node.value = score[end]
        return node

    if (iteration > N):  # 对棋盘评估
        node.evaluate()
        return node

    if (iteration % 2 == 0):
        return max_value(node, alpha, beta, iteration)

    else:
        return min_value(node, alpha, beta, iteration)

def max_value(node, alpha, beta, iteration):

    value = float('-inf')
    successors = node.get_successors() # 当前已是最新棋盘，据此来产生候选
    maxnode = node
    for i in successors:

        i.updateboard()   #更新棋盘
        getnode = get_value(i, alpha, beta, iteration+1)
        # StateDict[boardtolist(getnode.board)] = getnode.value
        i.restoreboard()  #复原棋盘

        if getnode.value > value:
            value = getnode.value
            i.value = value
            maxnode = i

        if value > alpha:
            alpha = value
        if value >= beta:
            return maxnode
    return maxnode

def min_value(node, alpha, beta, iteration):

    value = float('inf')
    minnode = node
    successors = node.get_successors()
    for i in successors:

        i.updateboard()
        getnode = get_value(i, alpha, beta, iteration+1)
        # StateDict[boardtolist(getnode.board)] = getnode.value
        i.restoreboard()

        if getnode.value < value:
            value = getnode.value
            i.value = value
            minnode = i

        if value < beta:
            beta = value
        if (value <= alpha):
            return minnode
    return minnode

def findcd(board, who):
    x = []
    y = []
    for a in range(len(board)):
        for b in range(len(board[a])):
            if board[a][b] == who:
                x.append(a)
                y.append(b)
    return x, y
def scatter():
    import matplotlib.pyplot as plt
    x1, y1 = findcd(board, 1)
    x2, y2 = findcd(board, 2)

    plt.scatter(x1, y1, s=200, c='orange')
    plt.scatter(x2, y2, s=200)
    ax = plt.gca()
    miloc = plt.MultipleLocator(1)
    ax.xaxis.set_minor_locator(miloc)
    ax.xaxis.set_major_locator(miloc)
    ax.yaxis.set_minor_locator(miloc)
    ax.yaxis.set_major_locator(miloc)
    plt.axis([0, pp.width, 0, pp.height])
    plt.grid(which='both')
    plt.show()
def combat():  ## test和testop下棋并把结果画出来
    import testop as tp
    import util as ut
    scatter()
    global board
    while True:
        (x, y) = brain_turn()
        board[x][y] = 1
        scatter()
        if ut.check_success(board, x, y) >= 0:
            break
        tp.board[x][y] = 2
        (x, y) = tp.brain_turn()
        board[x][y] = 2
        scatter()
        tp.board[x][y] = 1
        if ut.check_success(board, x, y) >= 0:
            break
# board[3][4]=2
# board[3][2]=0
# board[3][6]=1
# board[1][3]=2
# board[1][4]=1
# board[2][3]=2
# board[4][1]=2
# board[4][2]=1
# board[5][1]=2
# board[5][2]=1
# board[3][5]=2
# board[1][2]=1

# scatter()
# brain_turn()
# ####
# pyinstaller example.py pisqpipe.py Threat.py Node.py util.py --name pbrain-pyrandom.exe --onefile
# ####

# board[3][1]=1
# board[6][1]=2
#
# board = [[0 for i in range(MAX_BOARD)] for j in range(MAX_BOARD)]

# scatter()
# print(brain_turn())
combat()



# (x, y) = brain_turn()
# board[x][y] = 1
# scatter()
# board[11][11] = 2
# (x, y) = brain_turn()
# board[x][y] = 1
# scatter()
