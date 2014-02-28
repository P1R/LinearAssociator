def Str2Bin(s):
    A=[bin(ord(c))[2:] for c in s]
    B=[]
    for i in range(len(A)):
        B.append([int(d) for d in str(A[i])])	
    return B
    
    
