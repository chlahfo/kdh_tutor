#include <stdio.h>

int main(void){
    int a = 101;

    if (a < 0){
        a = -a;
    }
    if (a % 2 == 0){
        a = 2;
    } else {
        a = 1;
    }

    return 0;
}