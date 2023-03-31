#include <stdio.h>
#include <string.h>

int main(void){
    int max_num = 15;
    int view_num = 5;
    int i = view_num;
    int str_len;
    char str[max_num + 1];
    char str2[max_num + 1];
    
    printf("write word : ");
    fgets(str, sizeof(str), stdin);
    str[strlen(str) - 1] = '\0';
    strcpy(str2, str);
    
    str_len = strlen(str);

    if(str_len > view_num){        
        while(str[i] != '\0'){
            str2[i] = '*';
            i++;
        }
    }

    printf("writed word : %s, hidden word : %s", str, str2);
    
    return 0;
}