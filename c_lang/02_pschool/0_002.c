#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

//몫 구하기
int solution(int num1, int num2);
int solution_use_p(int *pn1, int *pn2);


int main(void){
    return 0;
}

int solution(int num1, int num2) {
    int answer = solution_use_p(&num1, &num2);
    return answer;
}
int solution_use_p(int *pn1, int *pn2){
    return *pn1 / *pn2;
}

// int solution(int num1, int num2) {
//     int answer = num1 / num2;
//     return answer;
// }