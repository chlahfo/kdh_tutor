#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main(void){
    int a, b, res;
    char mat[200];
    char test1[200];
    char test2[200];

    scanf("%s", test1); 
    printf("test1: %s", test1);
    scanf("%s", test2); 
    printf("test2: %s", test2);
    
    printf("input a: ");
    scanf("%d", &a);
    
    printf("%d\n", a);

    printf("operation +, -, / , *: ");
    //scanf("%c", &mat);
    fgets(mat, 2, stdin);
    printf("%s\n", mat);

    printf("input b: ");
    scanf("%d", &b);
    printf("%d", b);
    
    
    if(mat[0] == '+'){
        printf("%d + %d = %d\n", a, b, a + b);
    }else if(mat[0] == '-'){
        printf("%d - %d = %d\n", a, b, a - b);
    }else if(mat[0] == '/'){
        printf("%d / %d = %d\n", a, b, a / b);
    }else if(mat[0] == '*'){
        printf("%d * %d = %d\n", a, b, a * b);
    }else{
        printf("%c", mat[0]);
        printf("input error. please restart program.\n");
    }
    printf("\nput 함수 테스트 : ");
    gets(mat);
    fgets(mat, 200, stdin);
    puts(mat);
    printf("%s", mat);

    return 0;
}