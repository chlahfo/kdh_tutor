// 코드
#include <stdio.h>
#include <math.h>

int main(void) {

	int n, N = 0;    // n : 입력할 수, N : n - i 값을 저장할 변수 (i = 1, 2, 3 ...)
	int count1 = 0, count2 = 0;    // count1 : 자릿수 판단 변수, count2 : 신기한 수 개수 변수
	int a = 0, res = 0;    // a : 각 자리수의 수, res : 각 자리수의 총합
	
    n = 18;
	for (int j = n; j > 0; j--) {
		N = j;    // N 값 초기화
		while (N != 0) {    // n의 자릿수 판단
			N /= 10;    // n을 10으로 계속 나누다가 n이 0이면 셈 종료
			++count1;
		}
		N = j;    // N 값 초기화
		for (int i = count1 - 1; i >= 0; i--) {
			a = N / (int)pow(10.0, (double)i);    // 각 자릿수의 수 판단
			res += a;    // 각 자리수의 총합 누적
			N %= (int)pow(10.0, (double)i);    // 다음 자릿수를 파악하기 위해 판단한 자릿수는 제외 
		}
		N = j;    // N 값 초기화
		if (N % res == 0)count2++;    // N값을 각  자릿수의 총합으로 나누었을시 나누어 떨어지면 신기한 수로 판단
		res = 0;    // 다음 계산을 위해 res 값 초기화
		count1 = 0;    // 다음 계산을 위해 count1 값 초기화
	}
	printf("%d", count2);
	
	return 0;
}

/*scanf("%d", &n);    // 값 입력*/