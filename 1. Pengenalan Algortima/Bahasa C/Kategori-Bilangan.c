#include <stdio.h>

int main () {
    // Deklarasi Variabel
    int number;

    printf("Masukan bilangan bulat: ");
    // input bilangan bulat
    scanf ("%d", &number);

    // Cek apakah bilangan tersebut Positif, Negatif atau Nol

    if (number > 0 ) {
        printf ("Bilangan %d: positif\n", number);
    }
    else if (number < 0 ) {
        printf ("Bilangan %d: Negatif\n", number);
    }
    else {
        printf ("Bilangan %d : Nol\n", number);

    }
    return 0; 
}