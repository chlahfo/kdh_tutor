#include <stdio.h>
#include <string.h>
//예상 답 5, 6번 --> 정답 2번 5번, 6번
//배열에 붙여 넣을 공간이 부족해서 2번도 틀린것
int main(void){
    char str[] = "lion";
    char *ps = "king";
    int chk;

    /*
    strcpy(str, "cat");
    printf("%s", str);
    */

    /*
    strcat(str, ps);
    printf("%s", str);
    */

    chk = strcmp(ps, str);
    printf("%d\n", chk);

    chk = strlen(ps);
    printf("%d\n", chk);
    
    return 0;
}