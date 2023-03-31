#include <stdio.h>

int main(void){
    char *pa = "apple";
    char ary[] = "banana";
    char *pary[4];
    int i;

    pary[0] = "what..";
    pary[1] = pa;
    pary[2] = ary;
    pary[3] = "mango";
    //pary[4] = "orange";

    for (i = 0; i < 4; i ++){
        printf("%s\n", *(pary+i));
    }

    return 0;
}
//4 > 배열 요소가 4개인 배열이므로 첨자는 0부터 3까지만 사용해야 한다.