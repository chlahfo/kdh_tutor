#include <stdio.h>

int main(void){
    int seats = 70;
    int audience = 65;
    double rate = (double)audience/(double)seats * 100;

    printf("%.1lf%%\n", rate);

    return 0;
}