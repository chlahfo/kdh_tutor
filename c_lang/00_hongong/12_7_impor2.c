#include <stdio.h>
void my_gets(char *ps){
    char ch;
    while((ch = getchar()) != '\n'){
        *ps = ch;
        ps ++;
    }
    *ps = '\0';
}
int main(void){
    char str[80];
    my_gets(str);
    printf("%s",str);
    
    return 0;
}