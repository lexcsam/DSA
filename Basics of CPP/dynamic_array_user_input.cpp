#include <iostream>
using namespace std;
int main() {
    int length;

    // Ask the user for the length of the array
    cout << "Enter the length of the array: ";
    cin >> length;

    // Create a dynamic array using 'new'
    int* dynamicArray = new int[length];

    // Now you can use the 'dynamicArray' just like a regular array
    // For example, you can initialize and print the elements:

    cout << "Enter " << length << " elements:\n";
    for (int i = 0; i < length; ++i) {
        cin >> dynamicArray[i];
    }

    cout << "Array elements are: ";
    for (int i = 0; i < length; ++i) {
        cout << dynamicArray[i] << " ";
    }
    cout << endl;

    // Don't forget to release the memory when you're done with the array
    delete[] dynamicArray;

    //because we deleted the array , following code will give garbage values
     for (int i = 0; i < length; ++i) {
        cout << dynamicArray[i] << " ";
    }
    cout << endl;

    return 0;
}
