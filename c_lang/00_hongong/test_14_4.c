#include <stdio.h>

int main(void){
    char *animals[] = {"apple", "pear", "peach", "banana", "melon"};
    int len = sizeof(animals) / sizeof(animals[0]);
    int i;
    for (i = 0;i < len; i ++){
        printf("%s\n", *(animals + i));
    }
    
    return 0;
}