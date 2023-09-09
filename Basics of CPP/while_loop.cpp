#include<bits/stdc++.h>
using namespace std;
int main() {
    string s1;
    cout << "Enter a string : " << "\n";
    getline(cin, s1);
    int i;
    while(i <= 10) {
        cout << s1 << "\n";
        i++;
    }
    //now , for practricality , we generally use do while loops so that our code gets executed at least one time
    //so , let's see how to use do while loops
    //do while loops are used when we want to execute our code at least one time
    int j = 5;
    do {
        cout << "Hello World" << "\n";
        j++;
    } while(j <= 5);

    return 0;
}