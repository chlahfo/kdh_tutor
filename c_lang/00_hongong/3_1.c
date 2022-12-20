#include <stdio.h>

int main(void){
    int a;
    int b,c;
    double da;
    char ch;

    a = 10;
    b = a;
    c = a + 20;
    da = 3.5;
    ch = 'A';
    
    printf("Variable 'a' value.: %d\n", a);
    printf("Variable 'b' value.: %d\n", b);
    printf("Variable 'c' value.: %d\n", c);
    printf("Variable 'da' value: %.1lf\n", da);
    printf("Variable 'ch' value: %c\n", ch);

    a++;
    printf("%d %d\n", a, b);

    return 0;
}