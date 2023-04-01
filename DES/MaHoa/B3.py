# Viết hàm R1 = E(R0) mở rộng nửa phải chuỗi số 32 bit (R) thành 2 nửa 32 bit trái (L) và phải (R)

def hex_to_bin(s):
    mp = {
        '0' : "0000",
        '1' : "0001",
        '2' : "0010",
        '3': "0011",
        '4': "0100",
        '5': "0101",
        '6': "0110",
        '7': "0111",
        '8': "1000",
        '9': "1001",
        'A': "1010",
        'B': "1011",
        'C': "1100",
        'D': "1101",
        'E': "1110",
        'F': "1111"
    }
    bin = ""
    for i in range(len(s)):
        bin = bin + mp[s[i]]
    return bin

def bin_to_hex(s):
    mp = {
        "0000": '0',
        "0001": '1',
        "0010": '2',
        "0011": '3',
        "0100": '4',
        "0101": '5',
        "0110": '6',
        "0111": '7',
        "1000": '8',
        "1001": '9',
        "1010": 'A',
        "1011": 'B',
        "1100": 'C',
        "1101": 'D',
        "1110": 'E',
        "1111": 'F'
    }
    hex = ""
    for i in range(0, len(s), 4):
        ch = ""
        ch = ch + s[i]
        ch = ch + s[i + 1]
        ch = ch + s[i + 2]
        ch = ch + s[i + 3]
        hex = hex + mp[ch]
    return hex

def permute(k, arr, n):
    permutation = ""
    for i in range(0, n):
        permutation = permutation + k[arr[i] - 1]
    return permutation

#bảng mở rộng
Exp_table = [
    32,  1,  2,  3,  4,  5,  
     4,  5,  6,  7,  8,  9,  
     8,  9, 10, 11, 12, 13, 
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21, 
    20, 21, 22, 23, 24, 25, 
    24, 25, 26, 27, 28, 29, 
    28, 29, 30, 31, 32,  1
]

R1 = "70F9CE0D"

def encrypt(pt):
    pt = hex_to_bin(pt)
    E_R = permute (pt, Exp_table, 48)
    pt = bin_to_hex(E_R)
    print(pt)

encrypt(R1)

