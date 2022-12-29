#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

//두 수의 곱
int solution(int num1, int num2);
int solution_ex(int *pn1, int *pn2);

int main(void){
    return 0;
}
int solution(int num1, int num2) {
    int answer = solution_ex(&num1, &num2);
    return answer;
}
int solution_ex(int *pn1, int *pn2){
    return *pn1 * *pn2;
}