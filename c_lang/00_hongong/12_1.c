#include <stdio.h>

int main(void){
    printf("apple�� ����� ���� �ּ� ��: %p\n", "apPle");       //�ּ� �� ���
    printf("�� ��° ������ �ּ� ��: %p\n", "apPle" + 1);        //�ּ� �� ���
    printf("ù ��° ���� : %c\n", *("apPle"));                 //���� ���� ����
    printf("�� ��° ���� : %c\n", *("apPle"+1));               //������ �����
    printf("�迭�� ǥ���� �� ��° ���� : %c\n", "apPle"[2]);    //�迭 ǥ����
    
    return 0;
}