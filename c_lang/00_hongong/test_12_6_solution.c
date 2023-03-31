#include <stdio.h>
#include <string.h>

int main(void){
    char str[80];
    char res_str[80];
    char *star = "*****";
    int len;
    printf("input word : ");
    scanf("%s", str);
    len = strlen(str);
    if (len <= 5){
        strncpy(res_str, str, 5);
    }else{
        strncpy(res_str, str, 5);
        res_str[5] = '\0';
        strncat(res_str, star, len -5);
    }
    printf("inputed word : %s, res word : %s\n", str, res_str);
    return 0;
}

//353p