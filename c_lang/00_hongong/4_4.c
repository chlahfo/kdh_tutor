#include <stdio.h>

int main(void){
    int a = 5, b = 5;
    int pre , post;

    pre = (++a) * 3;//++ 한뒤 *3
    post = (b++) * 3;//*3 한 뒤 ++(가장 마지막에 계산됨.)

    printf("초깃값 a = %d, b = %d\n", a, b);
    printf("전위형: (++a) * 3 = %d, 후위형: (b++) * 3 = %d\n", pre, post);

    return 0;
}
