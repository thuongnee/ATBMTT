#include<iostream>
#include<fstream>
#include<map>
#define f first
#define s second
using namespace std;
map<char, char>M;
void reverKey(string key) {
	int d = 0;
	for (char i = 'A'; i <= 'Z'; i++) M[i] = key[d++];
}
void inreverKey(string key) {
	char d = 'A';
	for (auto x : key) M[x] = d++;
}

string monoalphabeticEncyption(string input, string key) {
	reverKey(key);
	string output = "";
	for (int i = 0; i < input.length(); i++) output += M[input[i]];
	return output;
}
string monoalphabeticDecyption(string input, string key) {
	inreverKey(key);
	string output = "";
	for (int i = 0; i < input.length(); i++) 	output += M[input[i]];
	return output;
}
bool checkKey(string key) {
	if (key.length() != 26) return false;
	map<char, bool> M;
	for (int i = 0; i < key.length(); i++) {
		if (M[key[i]] == false) {
			M[key[i]] = true;
		}
		else if (M[key[i]] == true) {
			return false;
		}
	}
	return true;
}
int main()
{
	string input, key, output = "";
	ifstream in("mahoachudon.txt");
	in >> input;
	in >> key;
	if (checkKey(key) == false) {
		cout << "Key khong hop le";
		return 0;
	}
	in.close();
	cout << "input: " << input << "\nkey: " << key << endl;
	output = monoalphabeticEncyption(input, key);
	cout << "Monoalphabetic Encyption : " << output << endl;
	cout << "Monoalphabetic Decyption : " << monoalphabeticDecyption(output, key);
}
