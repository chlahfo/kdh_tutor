#include <stdio.h>

int main(void){
    char ch;
    int i;

    for (i = 0;i<3;i++){
        scanf("%c", &ch);
        printf("%c\n", ch);
    }
    printf("\n=================\n");
    while(1){
        scanf("%c", &ch);
        if(ch =='\n') break;
        printf("%c\n", ch);
    }
    return 0;
}