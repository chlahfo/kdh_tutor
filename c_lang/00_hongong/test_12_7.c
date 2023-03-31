#include <stdio.h>
#include <string.h>

int main(void){
    char str1[100];
    char str2[100];
    char str3[100];
    
    printf("input 3 word : ");
    
    scanf("%s",str1);
    scanf("%s",str2);
    scanf("%s",str3);

    if((strcmp(str1, str2) <= 0)&& (strcmp(str1, str3) <= 0)){
        if((strcmp(str2, str3) <= 0)){
            printf("%s %s %s", str1, str2, str3);
        }else{
            printf("%s %s %s", str1, str3, str2); 
        }
    }else if((strcmp(str2, str1) <= 0)&& (strcmp(str2, str3) <= 0)){
        if((strcmp(str1, str3) <= 0)){
            printf("%s %s %s", str2, str1, str3);
        }else{
            printf("%s %s %s", str2, str3, str1);
        }
    }else{
        if((strcmp(str1, str2) <= 0)){
            printf("%s %s %s", str3, str1, str1);
        }else{
            printf("%s %s %s", str3, str2, str1);
        }
    }
    return 0;
}