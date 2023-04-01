# Viết hàm XR1K = XOR(R1, Ks) thực hiện phép XOR bit hai chuỗi số 48 bit R1 và Ks

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

def xor(a, b):
    ans = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            ans = ans + "0"
        else:
            ans = ans + "1"
    return ans

def encrypt(pt, ks):
    pt = hex_to_bin(pt)
    ks = hex_to_bin(ks)
    XR1K = xor(pt, ks)
    print(bin_to_hex(XR1K))

R1 = "BA17F3E5C05A"
Ks = "E127CAD84517"

encrypt(R1, Ks)