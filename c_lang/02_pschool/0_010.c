#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
int solution2(int *pn);
int solution(int n);
int main(void){

    printf("%d", solution(10));

    int array0[4] = {1,2,3,4};
    printf("%d", array0[-1]);
    return 0;
}
int solution2(int *pn){
    int sum = 0;
    int half = *pn / 2;

    sum = (half + 1) * half;
    
    return sum;
}
int solution(int n) {
    int answer = solution2(&n);
    return answer;
}
