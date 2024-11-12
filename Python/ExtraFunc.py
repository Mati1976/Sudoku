import numpy as np

def NumToBin2 (r,c,num):    
    if (num // 10) != 0:
        NumList= np.zeros(r, dtype=int)
        S = len(str(num))
        for i in range(S):
            NumList[r -(num % 10)] = 1
            num = num // 10
        BinNum = NumList
    else: 
        BinNum = np.zeros(r, dtype=int)

    return BinNum