#include <stdio.h>
#include <string.h>

int main(void){
    char str[80];
    printf("������ ���Ե� ���ڿ� : ");
    fgets(str, sizeof(str), stdin);
    printf("�Էµ� ���ڿ��� %s�Դϴ�\n", str);
    str[strlen(str)-1] = '\0';
    
    return 0;
}