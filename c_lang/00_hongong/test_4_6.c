#include <stdio.h>

int main(void){
    int hour, min, sec;
    double time = 3.76;

    hour = time;
    time -= hour;
    min = time * 60;
    time -= (min/60);
    sec = time * 60;

    printf("3.76시간은 %d시간 %d분 %d초입니다.", hour, min, sec);

    return 0;
}