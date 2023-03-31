#include <stdio.h>

int main(void){
    char animal[5][20];
    int i;
    int count;
 
    count =  sizeof(animal)/ sizeof(animal[0]);
    
    for (i = 0; i < count; i++){
        scanf("%s", animal[i]);
    }
    printf("\n");
    for (i = 0; i < count; i++){
        printf("%20d\n", (animal + i));
        //%s일 시 정상 출력된다.  %s는 문자열을 받는 형식 지정자이며, 문자열은 곧 문자 배열이므로 주소이다. 즉 %s 일 때, 주소를 적어넣으면
        //널 문자가 나올 때 까지 출력되는 것이다. 하지만 그 외에는 단순하게 주소가 찍히는 형식이며 %d로 찍을 경우는
        //주소가 20씩 증가되어 나온다. animal 은 첫번째 배열의 주소이므로 +1 을 하였을 경우 첫번째 배열 요소의 크기만큼 늘어난다.
        //즉 [20]의 크기만큼 늘어나게되어(char 배열이므로..) 20씩 증가하게 되는 것이다.
        //그럼 아래에 scanf를 d로 받았을 때의 표현 방식에 대하여 생각해보자.
    }
    return 0;
}