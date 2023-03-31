#include <stdio.h>

char my_strlen(char *pa);
int main(void){
    char str[100] = "banana";
    int num = my_strlen(str);
    printf("%d\n", num);

    return 0;
}

char my_strlen(char *pa){
    int count = 0;

    while (*pa != '\0'){
        count++;
        pa++;      
    }
    

    return count;
}