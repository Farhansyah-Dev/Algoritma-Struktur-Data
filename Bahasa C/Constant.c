#include <stdio.h>

int main () {

    int myNumber;

    // const int myNumber = 12;
    // myNumber = 13; //Erorr Result karena nilai Constant tidak bisa dirubah.

    /*Praktik yang baik dengan menggunakan nama variable dengan huruf kapital
    diawal
    example:
    */
    const int MYBIRTDAY = 2004;

    if (MYBIRTDAY <= 1999 && MYBIRTDAY >= 1980) {
        printf("Anda adalah Generasi Milenial.");
    }
    else if (MYBIRTDAY >= 2000 && MYBIRTDAY <= 2006) {
        printf ("Anda adalah Generasi Gen Z");
    }
    else {
        printf ("Anda adalah Generasi Baru");
    }

printf ("%d myNumber is: ", myNumber);
}

