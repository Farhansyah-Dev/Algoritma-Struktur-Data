#include <stdio.h>

int ExampleFor (int number) {
    int start;
    for (start = 1; start <= number; start++) {
        printf ("%d Example Looping for dalam bahasa C\n", number);
    }
}

int ExampleWhile (int number) {
    int start = 1;
    while (start <= number) {
        printf ("%d Example Looping While dalam bahasa C\n", number);
        start += 1;
    }
}


int main () {

    ExampleFor(5);
    ExampleWhile(5);
    printf ("Looping end...");
}