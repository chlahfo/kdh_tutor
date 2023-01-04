#include <stdio.h>

int main(void){
    int ary[3] = {10, 20, 30};
    int *pa = ary;
    int i;

    printf("배열의 값: ");
    for (i = 0; i < 3; i++){
        printf("%d ", *pa);
        pa++;
    }
    printf("\n");
    return 0;
}
//보통 배열의 범위를 넘어갈 수 있기 때문에 배열을 한번 포인터로 받으면 그 값을 변화시키진 않는다. 다만 가능하다는 것 정도만 숙지하기.