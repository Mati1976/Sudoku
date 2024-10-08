import numpy as np


def MatShape(r,c,m,n,mat):
    
    res = mat[r:r+m,c:c+n]
    
    return res

def square(a,b,SmallRow,SmallCol,mat):
    res=MatShape(a*SmallRow,b*SmallCol,SmallRow,SmallCol,mat)
    
    return res

def Col(b,mat):

    res=MatShape(0,b,9,1,mat)
    return res

def Row(a,mat):
    
    res=MatShape(a,0,1,9,mat)
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
    NUMBs = nums(SmallRow,SmallCol, block)
    for i in range(0, SmallRow):
        for j in range(0, SmallCol):
            if ((block[i][j]) // 10 != 0):
                block[i][j] = DelMultiItems(NUMBs,block[i][j])
    return block

def RowSolvBasic (Row,Col, row):
    NUMBs = nums(1,Col, row)
    for j in range(0, Col):
        if ((row[0][j]) // 10 != 0):
            row[0][j] = DelMultiItems(NUMBs,row[0][j])
    return row

def ColSolvBasic (Row,Col, col):
    NUMBs = nums(Row,1, col)
    for i in range(0, Row):
        if ((col[i][0]) // 10 != 0):
            col[i][0] = DelMultiItems(NUMBs,col[i][0])
    return col

def MatBlockSolvBasic(Rows,Columns,SmallRow,SmallCol,mat):
    for i in range(0, Rows // SmallRow):
        for j in range(0, Columns // SmallCol ):
            BlockSolvBasic (SmallRow,SmallCol, square(i,j,SmallRow,SmallCol,mat))
            
            
def MatRowSolvBasic(Rows,Columns,mat):
    for j in range(0, Columns):
        RowSolvBasic (Rows,Columns, Row(j,mat))

def MatColSolvBasic(Rows,Columns,mat):
    for i in range(0, Rows):
        ColSolvBasic (Rows,Columns, Col(i,mat))

            
mat = np.array([[0,7,0,0,5,0,0,6,0],
 [4,0,0,9,0,3,0,0,1],
 [0,0,8,0,0,0,3,0,0],
 [0,5,0,0,0,0,0,4,0],
 [1,0,0,0,0,0,0,0,9],
 [0,2,0,0,0,0,0,1,0],
 [0,0,4,0,0,0,7,0,0],
 [9,0,0,1,0,7,0,0,6],
 [0,8,0,0,3,0,0,5,0]])


mat = np.array([[0,2,0,0,1,0],
 [5,0,0,2,0,6],
 [0,0,4,0,2,0],
 [0,6,0,3,0,0],
 [4,0,3,0,0,2],
 [0,1,0,0,5,0]])


##print(mat[0:3])
##print(mat[0:2,0:4])

#print(mat[0:2,0:4].shape)
rows = mat.shape[0]
columns = mat.shape[1]

if ((rows==9 and columns==9)) :
    SR=3
    SC=3
else:
    if ((rows==6) and (columns==6)) :
        SR=2
        SC=3
    else:
        print('Error!')
        
            
        
    

res = init(rows,columns,mat)

print(res)





#print(mat2)
#print(type(mat2))
#print(mat2.shape)

#print(res.shape)
#print(square(0,0,res))
#print(MatShape(0,0,4,1,res))#print(MatShape(0,0,1,4,res))




temp = square (2,1,SR,SC,res)
print('temp')
print(temp)
tempnums = nums(SR,SC,temp)
NewTemp = BlockSolvBasic (SR,SC, temp)
print('newtemp:')
print(NewTemp)

print(tempnums)
print('temp:')
print(temp)

print('mat:')
print(res)

MatBlockSolvBasic(rows,columns,SR,SC,res)
print('new mat:')
print(res)

MatRowSolvBasic(rows,columns,res)
print('new mat2:')
print(res)

MatColSolvBasic(rows,columns,res)
print('new mat3:')
print(res)
MatRowSolvBasic(rows,columns,res)
print('new mat4:')
print(res)

MatColSolvBasic(rows,columns,res)
print('new mat5:')
print(res)

MatBlockSolvBasic(rows,columns,SR,SC,res)
print('new mat6:')
print(res)
MatRowSolvBasic(rows,columns,res)
print('new mat7:')
print(res)

MatColSolvBasic(rows,columns,res)
print('new mat8:')
print(res)

MatBlockSolvBasic(rows,columns,SR,SC,res)
print('new mat9:')
print(res)
#tempd = digitize(temp[0,0])

##print(numberize(tempd))
##ind = np.where(tempd == 3)[0][0]
##print(ind)
##tempd= np.delete(tempd,ind)
##print(tempd)
##print(numberize(tempd))

NewNum=DelItem(2,123456)
NewNum2= DelItem(5,NewNum)

print ('test')
NewNum3 = DelMultiItems([2,5],12346)
print(NewNum3)

row1= Row(0,res)
print('row:')
print(row1)
print('nums:')
print(nums(1,6, row1))
print(type(nums(1,6, row1)))
RowSolvBasic (rows,columns, row1)
print('row new:')
print(row1)


##print(Row(5,res))
##print(Col(4,res))
#rint(res[0:3,0:3].shape)

#print(fill(6))
