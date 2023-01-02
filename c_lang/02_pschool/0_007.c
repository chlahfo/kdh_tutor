//두 수의 합
#include <stdio.h>
int solution(int num1, int num2);
int solution2(int *p_n1, int *p_n2);
int main(void){
    return 0;
}

int solution2(int *p_n1, int *p_n2){
    return *p_n1 + *p_n2;
}
int solution(int num1, int num2) { 
    int answer = solution2(&num1, &num2);

    return answer;
}