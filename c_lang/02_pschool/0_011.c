//머쓱이보다 키 큰 사람
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int array[], size_t array_len, int height);
int sol2(int *array, int *array_len, int *height);
int main(void){
    int aaa[] = {149, 180, 192, 170};
    int height = 167;
    int size = sizeof(aaa) / sizeof(aaa[0]);
    int res = solution(aaa, size, height);
    printf("%d\n", res);

    return 0;
}

// array_len은 배열 array의 길이입니다.
int sol2(int *array, int *array_len, int *height){
    int res = 0;
    int i;
    for (i = 0; i < *array_len; i ++){
        if (array[i] > *height){
            res++;
        }
    }
    return res;
};
int solution(int array[], size_t array_len, int height) {
    int answer = sol2(array, &array_len, &height);
    return answer;
}