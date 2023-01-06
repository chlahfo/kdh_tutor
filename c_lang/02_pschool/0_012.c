//양꼬치
#include <stdio.h>
int solution(int n, int k);
int sol2(int *n, int *k);
int main(void){
    int aaa = solution(10, 3);
    printf("%d\n",aaa);
    return 0;
}
int sol2(int *n, int *k){
    int res = (*n * 12 + *k * 2 - *n/10 * 2)*1000;
    return res;
}
int solution(int n, int k){
    int answer = sol2(&n, &k);
    return answer;
}
// n인분과 음료수 k개 | 1인분에 12,000원, 음료수는 2,000원 | 10인분을 먹으면 음료수 하나를 서비스