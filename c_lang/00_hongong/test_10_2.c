#define _CRE_SECURE_NO_WARNING
#include <stdio.h>

void input_nums(int *lotto_nums);
void print_nums(int *lotto_nums);

int main(void){
    int lotto_nums[6];
    input_nums(lotto_nums);
    print_nums(lotto_nums);
    printf("\n");

    return 0;
}
void input_nums(int *lotto_nums){
    int i,j;
    int in_chk = 0;
    
    for (i = 0; i < 6; i++){
        do{
            in_chk = 0;
            printf("번호 입력(1~45): ");
            scanf("%d", lotto_nums + i);

            for (j = 0; j < i; j++){
                if(*(lotto_nums + i) == *(lotto_nums + j)){
                    in_chk = 1;
                    printf("같은 번호가 있습니다!\n");
                }
            }
        }while(in_chk == 1);
    }
}

void print_nums(int *lotto_nums){
    int i;
    printf("로또 번호 : ");
    for(i = 0; i < 6; i++){
        printf("%d   ", *(lotto_nums + i));
    }
}