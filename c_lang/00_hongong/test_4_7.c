#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void){
    double kg, cm, bmi;
    printf("몸무게를 입력해주세요(단위 kg): ");
    scanf("%lf", &kg);
    printf("키를 입력해주세요(단위 cm): ");
    scanf("%lf", &cm);

    bmi = kg / (cm * cm * 0.01* 0.01);
    printf("bmi:%lf\n", bmi);
    (bmi >= 20.0 && bmi < 25.0)?printf("표준입니다.\n"):printf("체중관리가 필요합니다.\n");

    return 0;
}