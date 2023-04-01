#include<string>
#include<iostream>
#include<fstream>
using namespace std;
string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
string RepeatKey(string input, string key) {
	string keyNew = key;
	int length = input.length();
	while (keyNew.length() < length) {
		for (int j = 0; j < input.length(); j++) {
			keyNew += input[j];
			if (keyNew.length() == length) break;
		}
	}
	return keyNew;
}
int position(char c) {
	if (c > 'Z') return c - 'a';
	return c - 'A';
}
string Vigenere_AutoKeyEncryption(string input, string key) {
	string cipher = "";
	int p, k, c;
	for (int i = 0; i < input.length(); i++) {
		p = position(input[i]);
		k = position(key[i]);
		c = (p + k) % 26;
		cipher += alphabet[c];
	}
	return cipher;
}
string Vigenere_AutoKeyDecryption(string input, string key) {
	string cipher = "";
	int p, k, c;
	for (int i = 0; i < input.length(); i++) {
		c = position(input[i]);
		k = position(key[i]);
		p = (c - k + 26) % 26;
		cipher += alphabet[p];
		key += alphabet[p];
	}
	return cipher;
}

int main()
{
	string input, k, key;
	int length;
	ifstream in("autokey.txt");
	in >> input;
	in >> key;
	in.close();

	cout << "input: " << input << "\nkey: " << key << endl;
	key = RepeatKey(input, key);
	cout << "Key new: " << key << endl;
	input = Vigenere_AutoKeyEncryption(input, key);
	cout << "Vigenere Encryption: " << input << endl;
	cout << "Vigenere Decryption: " << Vigenere_AutoKeyDecryption(input, key);
}
