//각도기
#include <stdio.h>
int solution2(int *angle);
int solution(int angle);

int main(void){

    return 0;
}
int solution2(int *angle){
    int answer = (*angle / 90) + (*angle > 90) + 1;
    //예각일 때 1, 직각일 때 2, 둔각일 때 3, 평각일 때 4
    return answer;
}
int solution(int angle) {
    return solution2(&angle);
}