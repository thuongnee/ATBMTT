# Viết hàm F = P(SXR1K) thực hiện hoán vị P
# Input: SXR1K - chuỗi số 32 bit
# Output: F - chuỗi số 32 bit là hoán vị của x theo ma trận P

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


per = [16,  7, 20, 21,
       29, 12, 28, 17,
       1, 15, 23, 26,
       5, 18, 31, 10,
       2,  8, 24, 14,
       32, 27,  3,  9,
       19, 13, 30,  6,
       22, 11,  4, 25]

def P(SXR1K):
    SXR1K = hex_to_bin(SXR1K)
    F = permute(SXR1K, per, 32)
    F = bin_to_hex(F)
    print(F)

SXR1K = "84C294A4"
P(SXR1K)