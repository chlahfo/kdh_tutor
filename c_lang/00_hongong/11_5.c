#include <stdio.h>

int main(void){
    int res;
    char ch;

    while(1){
        res = scanf("%c", &ch);
        if (res == EOF) break;// == -1(End of file)
        printf("%d ", ch);
    }      
    return 0;
}