#include <stdio.h>

int main(void){
    int hour, min, sec;     //1. 시간들 변수 설정
    double time = 3.76;     //2. 초기값 시간(단위:h) 설정

    hour = time;       //초기값에서 정수 부분만 추출. hour  가 int 형이므로 자동으로 추출됨.
    time -= hour;           //나머지 0.76h 거르기
    min = time * 60;        //time이 h 단위이므로 분단위로 바꾸기 위해 60으로 곱해줌. 단 min 은 int 형이므로 자동으로 소숫점 외 자리 추출됨.(time 은 m 단위)
    time = time * 60 - min; //time은 여전히 h단위이므로 m 단위로 변경하기 위해 60 곱해준 뒤, 아까의 min 부분(정수부분) - 해줌.
    sec = time * 60;        //나머지 sec만남았으므로 time을 sec 단위로 변경하기 위해 60을 곱해준 뒤 초에 넣어줌.

    printf("3.76시간은 %d시간 %d분 %d초입니다.\n", hour, min, sec);//출력

    return 0;
}