//중복된 숫자 개수
#include <stdio.h>
int solution(int *array, size_t array_len, int n);
int sol2(int *ary, int *ary_len, int *n);
int main(void){
    int bbb[] = {1, 1, 2, 3, 4, 5};
    int size = sizeof(bbb)/sizeof(bbb[0]);
    int aaa = solution(bbb, size, 1);
    printf("%d\n", aaa);

    return 0;
}
int sol2(int *ary, int *ary_len, int *n){
    int res = 0;
    int i;
    for (i = 0; i < *ary_len; i++){
        if(*(ary + i) == *n){
            res ++;
        }
    }
    return res;
}
int solution(int *array, size_t array_len, int n) {
    int answer = sol2(array, &array_len, &n);
    return answer;
}