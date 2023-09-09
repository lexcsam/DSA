#include<bits/stdc++.h>
using namespace std;
int main() {
    int arr[2][2];
    cout << "Enter 4 numbers : " << "\n";
    for(int i = 0; i < 2; i++) {
        for(int j = 0; j < 2; j++)
        cin >> arr[i][j];
    }
    cout << "The numbers you entered are : " << "\n" << arr[0][0] << "\n" << arr[0][1] << "\n" << arr[1][0] << "\n" << arr[1][1] << "\n";

}