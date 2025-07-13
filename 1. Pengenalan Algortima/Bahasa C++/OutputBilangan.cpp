#include <iostream>
using namespace std;

int main () {
    int number;

    cout << "Masukan Bilangan Bulat: ";
    cin >> number;

    if (number > 0) {
        cout << number <<" Positif"<<endl;
    }
    else if (number < 0 ) {
        cout << number <<" Negatif"<<endl;
    }
    else {
        cout << number <<" Nol"<<endl;
    }
}