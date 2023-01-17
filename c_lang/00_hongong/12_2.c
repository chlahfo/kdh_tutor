#include <stdio.h>

int main(void){
    char *dessert = "apple";

    printf("오늘 후식은 %s입니다.\n", dessert);
    dessert = "banana";
    //printf("내일 후식은 %s입니다 \n", dessert);
    while(*dessert != '\0'){
        putchar(*dessert);
        dessert++;
    }
    printf("\n");


    return 0;
}