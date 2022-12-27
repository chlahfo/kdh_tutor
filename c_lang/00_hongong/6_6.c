#include <stdio.h>

int main(void){
    int i;
    int sum = 0;
    for (i = 0; i <= 100; i++){
        if ((i % 3) == 0){
            continue;
        }
        sum += i;
        printf("%d\n", sum);
    }
    return 0;
}