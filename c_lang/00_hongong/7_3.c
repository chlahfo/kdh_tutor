#include <stdio.h>

void print_char(char ch, int count);

int main(void){
    print_char('@', 5);
    printf("\n");
    return 0;
}

void print_char(char ch , int count){
    int i;

    if (count > 100) return;
    for (i = 0; i < count; i++){
        printf("%c", ch);
    }

    return;
}