#include <iostream>
using namespace std;

int ExampleFor (int userInput) {
    for (int i = 1; i <= userInput; i++) {
        cout << "For in Language C++..."<<endl;
    }
    if (userInput <= 0) {
        cout << "Number not valid."<<endl;
    }
    else {
        cout <<userInput<< "Valid."<<endl;
    };
}

int ExampleWhile (int number2) {
    int start = 1;

    while (start <= number2) {
        cout << "This is While Loop in C++..."<<endl;
        start += 1;
    }
}



int main () {
    int userInput;

    cout << "Masukan Angka Buat Di looping dung: ";
    cin >> userInput;
    
    ExampleWhile (userInput);
    ExampleFor (userInput);
}