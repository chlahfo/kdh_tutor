#include <stdio.h>

int main(void){
    printf("%d\n", 'a');                //97
    printf("%d\n", 'A'-32);             //33
    printf("%d\n", 'b'-32);             //66
    printf("%d\n", 'A'+('b' - 'B'));    //97
    printf("%d\n", 97 - '0');           //49
    printf("%d\n", 97);                 //97

    return 0;
}