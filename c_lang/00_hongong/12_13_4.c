#include <stdio.h>
int my_strcmp(char *pa, char *pb);

int main (void){
    char aaa[100] = "apple";
    char bbb[100] = "banana";
    int chk = my_strcmp(aaa, bbb);

    printf("%d", chk);

    return 0;
}

int my_strcmp(char *pa, char *pb){
    while ((*pa == *pb) && (*pa != '\0')){
        pa++;
        pb++;
    }
    if(*pa > *pb){
        return 1;
    }else if(*pb > *pa){
        return -1;
    }else{
        return 0;
    }
}