#include <stdio.h>
int test1 = 200;
int test2 = 300;
int main(void){
    int a = 10, b = 20;

    printf("��ȯ �� a �� b �� ��: %d, %d\n", a, b);
    {
        int temp;

        temp = a;
        a = b;
        b = temp;

        printf("�� �ȿ����� a �� b �� ��: %d, %d\n", a, b);
    }
    printf("��ȯ �� a �� b �� ��: %d, %d\n", a, b);

    return 0;
}