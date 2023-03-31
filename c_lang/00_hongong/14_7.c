#include <stdio.h>

int main(void){
    int ary1[4] = {1, 2, 3, 4};
    int ary2[5] = {11, 12, 13};
    int ary3[5] = {21, 22, 23, 24, 25};
    int *pary[3] = {ary1, ary2, ary3};
    int i, j;

    for(i = 0; i < 3; i++){
        for (j = 0; j < 5; j++){
            printf("%5d", pary[i][j]);
        }
        printf("\n");
    }
    /*
        pary[i]의 요소는 각각 배열이다. 즉 ary1[j]는 pary[0][j]이므로 해당 반복문이 무리 없이 실행이 된다.
    */

   /*
        포인터 연산의 시점으로 보면 
        pary[2][2] == *(pary[2]+2);
        
   */
    return 0;
}