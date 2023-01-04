#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

//배열의 평균값
double solution(int *numbers, int numbers_len);
int main(void){
    int bbb[10] = {1,2,3,4,5,6,7,8,9, 10};
    double aaa = solution(bbb, 10);
    printf("%lf", aaa);

    return 0;
}
double solution(int *numbers, int numbers_len){
    int i, sum = 0;
    double answer;

    for (i = 0; i < numbers_len; i++){
        sum += *(numbers + i);
    }
    
    answer = (double)sum / numbers_len;

    return answer;
}

/*
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

//배열의 평균값
double solution(int *numbers, size_t numbers_len);
int main(void){
    double aaa = solution({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 10);
    printf("%lf", aaa);

    return 0;
}
double solution(int *numbers, size_t numbers_len){
    int i, sum = 0;
    double answer;

    for (i = 0; i < numbers_len; i++){
        sum += *(numbers + i);
    }
    
    answer = sum / numbers_len;

    return answer;
}
*/