#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void){
    int score[3][4];
    int total;
    double avg;
    int i, j;

    //self 도전
    for (i = 0; i < 3; i++){
        printf("4과목의 점수 입력(띄어쓰기로 구분): ");

        for(j = 0; j < 4; j++){
            scanf("%d", &score[i][j]);//배열에 접근할 때는 주소 연산자를 안써도 되지만, 배열 요소에 접근할 때는 주소 연산자를 사용해야한다. 

        }
    }
    for (i = 0; i < 3; i ++){
        total = 0;
        avg = 0;
        
        for (j = 0; j < 4; j ++){
            total += score[i][j];
        }
        avg = total / 4.0;

        printf("학생 %d의 총점: %d, 평균: %.2lf\n", i+1, total, avg);
    }
    return 0;
}

