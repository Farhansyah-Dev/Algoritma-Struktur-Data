#include <stdio.h>

int main () {

    int MyNum = 100 + 50;
    int Sum2 = MyNum + 250;
    int Sum3 = Sum2 + MyNum;

    printf("%d\n", MyNum);
    printf("%d\n", Sum2);
    printf("%d\n", Sum3);

    int VariableX = 10;
    VariableX += 2;
    VariableX -= 2;
    VariableX *= 2;
    VariableX /= 2;
    VariableX %= 2;
    VariableX &= 2;
    VariableX |= 2;
    VariableX ^= 2;
    VariableX >>= 2;
    VariableX <<= 2;
    
    return 0;
}