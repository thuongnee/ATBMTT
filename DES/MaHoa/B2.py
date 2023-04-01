# Viết hàm SPLIT(x, L, R) tách chuỗi số 64bit(x) thành 2 nửa 32 bit trái (L) và phải (R)

def SPLIT(x, L, R):
    L = x[0:8]
    R = x[8:16]
    print(L + "\n" + R)

x = "66581B2AE5B0BD6D"
L = R = ""
SPLIT(x, L, R)

