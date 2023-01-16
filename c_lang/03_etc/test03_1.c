// 코드
#include <stdio.h>

int main(void) {

	int n, N = 0;
	int count2 = 0;
	int a = 0, res = 0;
    double dN;
	
    //scanf("%d", &n);
    n = 234;
	for (int j = n; j > 0; j--) {
        N = j;
        

        while (N != 0){
            dN = (double)N;
            dN /= 10;
            N /= 10;
            a = (dN - N + 0.05) * 10;
            res += a;
        } 
        if (j % res == 0)count2++;
        res = 0;
	}
	printf("%d", count2);
	
	return 0;
}
