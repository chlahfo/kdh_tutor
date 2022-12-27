#include <stdio.h>

int sum(int n);

int main (void){
    sum(10);
    sum(100);
    return 0;
}

int sum (int n){
    int i;
    int temp = 0;
    for (i = 0; i <= n; i ++){
        temp += i;
    }

    printf("1부터 %d 까지의 합은 %d입니다.\n", n, temp);    
}