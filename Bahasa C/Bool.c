#include <stdio.h>

int main () {
    int PemilihanUmum = 18;
    int cekStatus;


    int age;
    printf ("Berapa Umur anda: ");
    scanf("%d", &age);

    if (age >= PemilihanUmum) {
        printf("Anda bisa mengikuti Pemilu 2028.");
    }
    else {
        printf("Maaf. belum bisa mengikut pemilu 2028.");
    }
}