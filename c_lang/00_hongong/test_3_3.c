#include <stdio.h>

int main(void){
    int kor, eng, mat, tot;
    kor = 70;
    eng = 80;
    mat = 90;
    
    tot = kor + eng + mat;
    printf("국어 점수: %d, 영어 점수: %d, 수학 점수: %d\n", kor, eng, mat);
    printf("총점: %d\n", tot);
    
    return 0;
}