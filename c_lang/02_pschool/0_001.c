//나머지 구하기

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int num1, int num2);
int solution_ex(int *pnum1, int *pnum2);

//포인터 연습
int main(void){
    return 0;
}

int solution(int num1, int num2) {
    int answer = solution_ex(&num1, &num2); 
    return answer;
}
int solution_ex(int *pnum1, int *pnum2){
    int res = *pnum1 % *pnum2;
    return res;
}

/*
int solution(int num1, int num2) {
    int answer = num1 % num2;
    return answer;
}
*/
