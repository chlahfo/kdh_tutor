#include <stdio.h>

char *my_strcat(char *pd, char *ps);

int main(void){
    char fruit_name[100] = "strawberry";
    char bread_name[100] = "pie";

    printf("%s�� %s�� ������??\n", fruit_name, bread_name);

    my_strcat(fruit_name, bread_name);

    printf("%s�� �ȴ�", fruit_name);
    return 0;
}

char *my_strcat(char *pd, char *ps){
    char *po = pd;

    while (*pd != '\0'){
        pd++;
    }

    while(*ps != '\0'){
        *pd = *ps;
        pd++;
        ps++;
    }
    *pd = '\0';

    return po;
}