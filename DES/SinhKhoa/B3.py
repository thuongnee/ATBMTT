#Viết hàm ShiftLeft(x,s) dịch vòng trái s bit đối với chuỗi số 28 bit (x)
#Input: x - chuỗi số 28 bit, s - số nguyên dương < 28
#Output: x - chuỗi số 28 bit đã dịch vòng trái s bit 
def hex_to_bin(s):
    mp = {'0': "0000",
          '1': "0001",
          '2': "0010",
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
          'F': "1111"}
    bin = ""
    for i in range(len(s)):
        bin = bin + mp[s[i]]
    return bin
 
# Binary to hexadecimal conversion
 
 
def bin_to_hex(s):
    mp = {"0000": '0',
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
          "1111": 'F'}
    hex = ""
    for i in range(0, len(s), 4):
        ch = ""
        ch = ch + s[i]
        ch = ch + s[i + 1]
        ch = ch + s[i + 2]
        ch = ch + s[i + 3]
        hex = hex + mp[ch]
 
    return hex

shift_table = [1, 1, 2, 2,
               2, 2, 2, 2,
               1, 2, 2, 2,
               2, 2, 2, 1]

def shift_left(k, nth_shifts):
    s = ""
    for i in range(nth_shifts):
        for j in range(1, len(k)):
            s = s + k[j]
        s = s + k[0]
        k = s
        s = ""
    return k

left = "88DE563"
right = "C9E654A"

for i in range(0, 16):
    left = hex_to_bin(left)
    right = hex_to_bin(right)
    # Shifting the bits by nth shifts by checking from shift table
    left = bin_to_hex(shift_left(left, shift_table[i]))
    right = bin_to_hex(shift_left(right, shift_table[i]))
    print("C" + str(i+1) + ": " + left + "\nD" + str(i+1) + ": " + right + "\n")