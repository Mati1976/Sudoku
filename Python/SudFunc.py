import numpy as np
StepCounter = 0

def MatShape(r,c,m,n,mat):
    
    res = mat[r:r+m,c:c+n]
    
    return res

def square(a,b,SmallRow,SmallCol,mat):
    res=MatShape(a*SmallRow,b*SmallCol,SmallRow,SmallCol,mat)
    
    return res

def Col(b,mat):

    res=MatShape(0,b,mat.shape[0],1,mat)
    return res

def Row(a,mat):
    
    res=MatShape(a,0,1,mat.shape[1],mat)
    return res

def init(r,c, mat):
    res = np.array([ [0]*c for i in range(r)])
    for i in range(0, r):
        for j in range(0, c):
            if mat[i][j] == 0:
                res[i][j] = fill(r)
            else:
                res[i][j] = mat[i][j]
    return res

def initBin(r,c, mat):
    res = np.array([ [0]*c for i in range(r)])
    for i in range(0, r):
        for j in range(0, c):
            if mat[i][j] == 0:
                res[i][j] = fill(r)
            else:
                res[i][j] = mat[i][j]
    return res

def NumToBin (r,c,num):    
    if (num // 10) != 0:
        NumList= np.zeros(r, dtype=int)
        S = len(str(num))
        for i in range(S):
            NumList[r -(num % 10)] = 1
            num = num // 10
        BinNum = NumList
    else: 
        BinNum = num

    return BinNum

def nums(SmallRow,SmallCol, block):
    resl = []
    for i in range(0, SmallRow):
        for j in range(0, SmallCol):
            if ((block[i][j]) // 10 == 0):
                resl.append(block[i][j])
    res = np.array(resl)
    return res

def fill(size):
    res = 0
    for i in range(size):
        res = res * 10 + i + 1
    return res

def digitize(num):
    digi = []
    while num > 0:
        digi.insert(0, num % 10)
        num = num // 10
    digits = np.array(digi)
    return digits

def numberize(dig):
    res = 0
    for item in dig:
        res = res * 10 + item 
    return res

def DelItem(dig,num):
    numd = digitize(num)
    NewNum = num 
    if (dig in numd):
        ind = np.where(numd == dig)[0][0]
        numd = np.delete(numd,ind)
        NewNum = numberize(numd)
    return NewNum

def DelMultiItems(digArr,num):
    Newnum = num
    for item in digArr:
        Newnum = DelItem(item, Newnum)
    return Newnum

def BlockSolvBasic (SmallRow,SmallCol, block):
    global StepCounter
    NUMBs = nums(SmallRow,SmallCol, block)
    for i in range(0, SmallRow):
        for j in range(0, SmallCol):
            if ((block[i][j]) // 10 != 0):
                block[i][j] = DelMultiItems(NUMBs,block[i][j])
    StepCounter += 1
    return block

def RowSolvBasic (Row,Col, row):
    global StepCounter
    NUMBs = nums(1,Col, row)
    for j in range(0, Col):
        if ((row[0][j]) // 10 != 0):
            row[0][j] = DelMultiItems(NUMBs,row[0][j])
    StepCounter += 1
    return row 

def ColSolvBasic (Row,Col, col):
    global StepCounter
    NUMBs = nums(Row,1, col)
    for i in range(0, Row):
        if ((col[i][0]) // 10 != 0):
            col[i][0] = DelMultiItems(NUMBs,col[i][0])
    StepCounter += 1
    return col

def MatBlockSolvBasic(Rows,Columns,SmallRow,SmallCol,mat):
    for i in range(0, Rows // SmallRow):
        for j in range(0, Columns // SmallCol ):
            BlockSolvBasic (SmallRow,SmallCol, square(i,j,SmallRow,SmallCol,mat))
    return 
            
            
def MatRowSolvBasic(Rows,Columns,mat):
    for j in range(0, Columns):
        RowSolvBasic (Rows,Columns, Row(j,mat))
    return 

def MatColSolvBasic(Rows,Columns,mat):
    for i in range(0, Rows):
        ColSolvBasic (Rows,Columns, Col(i,mat))
    return 

def RowScore (Row,Col, row):
    score = 0
    for j in range(0, Col):
        if ((row[0][j]) // 10 == 0):
            score += 1
    return score

def RowScoreVecInit (Rows,Columns,mat, RowScoreVec):
    
    for i in range(0, Rows):
        RowScoreVec[i,0] = RowScore (Rows,Columns, Row(i,mat))    
    return 

def ColScore (Row,Col, col):
    score = 0
    for i in range(0, Row):
        if ((col[i][0]) // 10 == 0):
            score += 1
    return score
def ColScoreVecInit (Rows,Columns,mat, ColScoreVec):
    
    for j in range(0, Columns):
        ColScoreVec[0,j] = ColScore (Rows,Columns, Col(j,mat))    
    return 

def BlockScore (SmallRow,SmallCol, block):
    score = 0
    for i in range(0, SmallRow):
        for j in range(0, SmallCol):
            if ((block[i][j]) // 10 == 0):
                score += 1
    return score

def BlockScoreMatInit (SmallRow,SmallCol,mat, BlockScoreMat):
    score = 0
    for i in range(0, mat.shape[0]//SmallRow):
        for j in range(0, mat.shape[1]//SmallCol):
            BlockScoreMat[i,j] = BlockScore (SmallRow,SmallCol, square(i,j,SmallRow,SmallCol,mat)) 
    return score 
