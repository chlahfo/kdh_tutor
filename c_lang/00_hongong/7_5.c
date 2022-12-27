#include <stdio.h>

void fruit(int);

int main(void){
    
    fruit(5);
    return 0;
}

void fruit(int limit){
    int cnt = limit;
    printf("apple\n");

    if (cnt > 1){
        fruit(cnt - 1);
    }
}