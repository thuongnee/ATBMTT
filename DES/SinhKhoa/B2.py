#Viết hàm SPLIT_Key(K1, C, D) tách chuỗi số 56 bit (K1) thành 2 nửa 28 bít trái (C) và phải (D)
#Input: K1 - chuỗi số 56bit
#Output: C, D - chuỗi số 28 bit

K1 = "8A7A43559D51FF"
C = ""
D = ""

def SPLIT_Key(K1, C, D):
    C = K1[0:7]
    D = K1[7:14]
    print(C + "\n" + D)

SPLIT_Key(K1, C, D) 