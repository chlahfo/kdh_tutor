#include <stdio.h>

int main(void){
    int i=0;
    char str[16];
    char str2[16];
    char alphabet;

    printf("input word: ");

    do{
        alphabet = getchar();
        
        str[i] = alphabet;
        
        if (i >= 5){
            str2[i] = '*';
        }else{
            str2[i] = alphabet;
        }
        
        i++;
    }while(alphabet != '\n' && i < 15);

    str[i-1] = '\0';
    str2[i-1] = '\0';

    printf("input word: %s, ress word: %s\n", str, str2);

    return 0;
}