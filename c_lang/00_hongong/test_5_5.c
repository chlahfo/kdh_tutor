#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main(void){
    int a, b, res;
    char mat;
    
    
    printf("input a: ");
    scanf("%d", &a);

    printf("operation +, -, / , *: ");
    scanf(" %c", &mat);

    printf("input b: ");
    scanf("%d", &b);
    
    
    if(mat == '+'){
        printf("%d + %d = %d\n", a, b, a + b);
    }else if(mat == '-'){
        printf("%d - %d = %d\n", a, b, a - b);
    }else if(mat == '/'){
        printf("%d / %d = %d\n", a, b, a / b);
    }else if(mat == '*'){
        printf("%d * %d = %d\n", a, b, a * b);
    }else{
        printf("%c", mat);
        printf("input error. please restart program.\n");
    }
    
    

    return 0;
}
