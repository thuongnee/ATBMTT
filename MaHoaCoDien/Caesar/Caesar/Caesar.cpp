#include <iostream>
#include <string>
#include <cstring>
#include <fstream>
using namespace std;
string CaesarEncyption(string input, int key) {
    string result = "";
    int length = input.length();
    for (int i = 0; i < length; i++)
        if (isupper(input[i]))
            result += char(int(input[i] + key - 65) % 26 + 65);
        else 
            result += char(int(input[i] + key - 97) % 26 + 97);
    return result;
}

string CaesarDecryption(string output, int key) {
    string result = "";
    int length = output.length();
    for (int i = 0; i < length; i++)
        if (isupper(output[i]))
            result += char(int(output[i] - key - 65 + 26) % 26 + 65);
        else 
            result += char(int(output[i] - key - 97 + 26) % 26 + 97);
    return result;
}


int main()
{
    int key, length;
    string input;
    //freopen("matma.txt", "r", stdin);
    ifstream in("matma.txt");
    in >> input;
    in >> key;  key %= 26;
    in.close();
    string output = CaesarEncyption(input, key);
    cout << "input: " << input << "\nkey: " << key << endl;
    cout << "Caesar Cipher: " << output << endl;
    cout << "Caesar Cipher Decryption: " << CaesarDecryption(output, key);

}