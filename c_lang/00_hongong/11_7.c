#include <stdio.h>

int main(void){
    int num, grade;

    printf("학번 입력 : ");
    scanf("%d", &num); 
    // 학번과 \n 이 저장됨. 만약 다음에 쓸 함수가 scanf 라고 한다면 아무것도 입력하지 않았을 때의 \n 값은 scanf 에서는 입력되서 나오지 않으므로 문제가 없지만, 다음 함수가 getchar를 쓴다면 문제가 된다. getchar 함수는 문자가 없는 상태에서도 \n를 입력받고 \n이 나타난 순간 함수가 끝나기 때문이다.
    getchar();
    //따라서 이와같이 함수를 실행해주면 남은 \n가 입력되고 바로 함수가 끝난다. 
    printf("학점 입력: ");
    grade = getchar();
    //그럼 여기서 학점입력이 오류없이 잘 해결될 수 있다.
    printf("학번 : %d, 학점 : %c", num, grade);

    return 0;
}