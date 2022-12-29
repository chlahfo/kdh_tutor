
//나이 출력
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int age);
int solution_p(int *p_age);

int main(void){
    return 0;
}
int solution_p(int *p_age){
    return (2022 - *p_age + 1);
}
int solution(int age) {
    int answer = solution_p(&age);
    return answer;
}