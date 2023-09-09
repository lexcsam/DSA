#include<bits/stdc++.h>
using namespace std;
int main() {
    string str;
    cout << "Enter a string : " << "\n";
    cin >> str;
    cout << "The string you entered is : " << str << "\n";
    int len = str.length();
    int size = str.size();
    // size and length are the same thing
    cout << "The size of the string is : " << size << "\n";
    cout << "The length of the string is : " << len << "\n";
    // to get the first character of the string
    cout << "The first character of the string is : " << str[0] << "\n";
    // to get the last character of the string
    cout << "The last character of the string is : " << str[len - 1] << "\n";
    // to get the middle character of the string
    cout << "The middle character of the string is : " << str[len / 2] << "\n";
    //to change the last character of the string
    str[len - 1] = 'a';
    cout << "The string after changing the last character is : " << str << "\n";
    //to get line input in a string
    string str1;
    cout << "Enter a string : " << "\n";
    getline(cin, str1);
    cout << "The string you entered is : " << str1 << "\n";
    //to get the substring of a string
    string str2 = str1.substr(0, 5);
    cout << "The substring of the string is : " << str2 << "\n";
    //to get the index of a character in a string
    int index = str1.find('a');
    cout << "The index of the character 'a' in the string is : " << index << "\n";
    //to get the index of a substring in a string
    int index1 = str1.find("is");
    cout << "The index of the substring 'is' in the string is : " << index1 << "\n";
    //to get the index of a substring in a string from a particular index
    int index2 = str1.find("is", 5);
    cout << "The index of the substring 'is' in the string from index 5 is : " << index2 << "\n";
    //to get the index of a substring in a string from a particular index in reverse
    int index3 = str1.rfind("is", 5);
    cout << "The index of the substring 'is' in the string from index 5 in reverse is : " << index3 << "\n";
    //to get the index of a character in a string from a particular index
    int index4 = str1.find('a', 5);

}
