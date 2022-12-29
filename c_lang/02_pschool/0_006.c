//숫자 비교하기
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
int solution(int num1, int num2);
int solution_p(int *pn1, int *pn2);

int main(void){
    return 0;
}
int solution_p(int *pn1, int *pn2){
    if (*pn1 == *pn2){
        return 1;
    }else{
        return -1;
    }    
}
int solution(int num1, int num2) {
    int answer = solution_p(&num1, &num2);
    return answer;
}