#include <stdio.h>
// int rec_func(int n);
// int main(void){
//     int r;
//     r = rec_func(10);
//     printf("%d\n", r);
//     return 0;
// }
// int sum = 0;
// int rec_func(int n){
//     sum += n;
//     if (n == 0) return sum;
//     rec_func(n - 1);   
// }

//답문
int rec_func(int n);
int main(void){
    int r;
    r = rec_func(10);
    printf("%d\n", r);
    return 0;
}
int sum = 0;
int rec_func(int n){
    sum += n;
    if (n == 0) return sum;
    rec_func(n - 1);   
}