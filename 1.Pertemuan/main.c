#include <stdio.h>

int main () {
    // Deklrasi Variabel
    int number;

    printf("Masukan bilangan bulat: ");
    // input bilangan bulat
    scanf ("%d", &number);

    // Cek apakah bilangan tersebut Positif, Negatif atau Nol

    if (number > 0 ) {
        printf ("Bilangan %d: positif\n");
    }
    else if (number < 0 ) {
        printf ("Bilangan %d: Negatif\n");
    }
    else {
        printf ("Bilangan %d : Nol\n");
    }
    return 0;
}