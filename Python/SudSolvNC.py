
#--------------------------------------------------------------------------Main---------------------------------------------------------------------------------------            
import numpy as np

import SudFunc as sf

mat2 = np.array(
[[0,7,0,0,5,0,0,6,0],
 [4,0,0,9,0,3,0,0,1],
 [0,0,8,0,0,0,3,0,0],
 [0,5,0,0,0,0,0,4,0],
 [1,0,0,0,0,0,0,0,9],
 [0,2,0,0,0,0,0,1,0],
 [0,0,4,0,0,0,7,0,0],
 [9,0,0,1,0,7,0,0,6],
 [0,8,0,0,3,0,0,5,0]])

mat3 = np.array(
[[0,0,0,0,5,1,0,0,0],
 [0,0,2,3,0,0,1,0,9],
 [0,0,1,9,8,2,3,0,0],
 [0,8,4,0,3,7,0,0,0],
 [0,6,0,0,4,0,0,7,0],
 [9,0,0,0,0,0,4,0,0],
 [2,0,0,5,0,0,6,3,0],
 [0,4,0,0,2,0,0,9,1],
 [0,9,0,1,0,0,0,4,0]])

mat4 = np.array(
[[5,0,2,0,9,0,1,0,0],
 [0,0,0,1,0,0,0,8,0],
 [3,0,0,0,0,6,0,0,2],
 [0,4,0,0,0,0,7,0,0],
 [6,0,0,0,0,0,0,0,1],
 [0,0,5,0,0,0,0,9,0],
 [9,0,0,7,0,0,0,0,4],
 [0,6,0,0,0,3,0,0,0],
 [0,0,7,0,2,0,5,0,3]])



mat = np.array(
[[0,2,0,0,1,0],
 [5,0,0,2,0,6],
 [0,0,4,0,2,0],
 [0,6,0,3,0,0],
 [4,0,3,0,0,2],
 [0,1,0,0,5,0]])


# Initializing our step counter
StepCounter = 0 

# Getting the shape of our matrix 
rows = mat.shape[0] 
columns = mat.shape[1]


# Setting up our block sizes based on the size of the Matrix (need to be updated for other cases ) 
if ((rows==9 and columns==9)) :
    SR=3
    SC=3
else:
    if ((rows==6) and (columns==6)) :
        SR=2
        SC=3
    else:
        print('Error!')


# Initializing our score vectors for the rows, columns, blocks and setting the MAx values for each 
ScoreRMax = columns
ScoreCMax = rows
ScoreBMax = SR*SC
ScoreMMAx = rows*columns

ScoreR = np.zeros((rows,1),).astype(int)
ScoreC = np.zeros((1,columns),).astype(int)
ScoreB = np.zeros((rows//SR,columns//SC),).astype(int)

# print (ScoreM)
res = sf.init(rows,columns,mat)

sf.RowScoreVecInit(rows,columns,res,ScoreR)
sf.ColScoreVecInit(rows,columns,res,ScoreC)
sf.BlockScoreMatInit(SR,SC,res,ScoreB)

print(ScoreR)
print(ScoreC)
print(ScoreB)


print('mat:')
print(res)
print('Step counter: '+str(StepCounter))
#print (ScoreR)
#print (ScoreC)
print(sf.RowScore (rows,columns,sf.Row(1,res)))
print(sf.ColScore (rows,columns,sf.Col(4,res)))
print(sf.BlockScore (SR,SC,sf.square(0,0,SR,SC,res)))

sf.MatBlockSolvBasic(rows,columns,SR,SC,res)
##print('test')
##print(sf.RowSolvBasic(rows,columns,sf.Row(1,res),StepCounter))
##print('test')
print('new mat:')
print(res)
print('Step counter: '+str(StepCounter))
sf.MatRowSolvBasic(rows,columns,res)
print('new mat2:')
print(res)
print('Step counter: '+str(StepCounter))

sf.MatColSolvBasic(rows,columns,res)
print('new mat3:')
print(res)

print(sf.RowScore (rows,columns,sf.Row(1,res)))
print(sf.ColScore (rows,columns,sf.Col(4,res)))
print(sf.BlockScore (SR,SC,sf.square(0,0,SR,SC,res)))

sf.MatRowSolvBasic(rows,columns,res)
print('new mat4:')
print(res)

sf.MatColSolvBasic(rows,columns,res)
print('new mat5:')
print(res)

sf.MatBlockSolvBasic(rows,columns,SR,SC,res)
print('new mat6:')
print(res)
sf.MatRowSolvBasic(rows,columns,res)
print('new mat7:')
print(res)

sf.MatColSolvBasic(rows,columns,res)
print('new mat8:')
print(res)

sf.MatBlockSolvBasic(rows,columns,SR,SC,res)
print('new mat9:')
print(res)
print('Step counter: '+str(StepCounter))



