#include <stdio.h>

int main(void){
    char str [20] = "apple";
    char *pa = str;
    char *pb = "pineapple";

    //printf("%s\n", "apple");
    printf("%s\n", str[0]);
    //printf("%s\n", pa);
    //printf("%s\n", pb + 4);

    //2번? a 만 나오지 않아?


    return 0;
}