#include <stdio.h>

int main(void){
    char *dessert = "apple";

    printf("���� �Ľ��� %s�Դϴ�.\n", dessert);
    dessert = "banana";
    //printf("���� �Ľ��� %s�Դϴ� \n", dessert);
    while(*dessert != '\0'){
        putchar(*dessert);
        dessert++;
    }
    printf("\n");


    return 0;
}