#include<iostream>
#include<string>
#include<fstream>
using namespace std;
string PermutationEncyption(string input, int key) {
	string output = "";
	int len_in = input.length();
	for (int i = 0; i < key; i++) {
		int j = i;
		while (j < len_in) {
			output += input[j];
			if (key - i - 1 == 0) break;
			j += 2*(key-i-1);
		}
	}

	return output;
}
int main()
{
	string input;
	int key;
	ifstream in("hoanvi.txt");
	in >> input;
	in >> key;
	in.close();
	cout << "input: " << input << "\nkey: " << key << endl;
	cout << "\nPermutation Encyption: " << PermutationEncyption(input, key) << endl;
	
}
