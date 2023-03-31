#include <stdio.h>

int main(void){
    int ary[5][6] = {
           {1, 2, 3, 4, 5},
           {6, 7, 8, 9, 10},
           {11, 12, 13, 14, 15},
           {16, 17, 18, 19, 20}
    };

    int i, j;

    for(i = 0; i < 4; i++)
    {
        for(j = 0; j < 5; j++)
        {
            ary[4][j] += ary[i][j];
            //각 열 끝 마다 4개씩 더해서 총 5개 열을 더함. 20번 더하기 필요
            ary[i][5] += ary[i][j];
            //각 행 끝마다 5개씩 더해서 총 4개 행을 구함. 20번 더하기 필요
            ary[4][5] += ary[i][j];
            //모든 수 20개를 다 더함
        }
    }
 
    for(i = 0; i < 5; i++)
    {
           for(j = 0; j < 6; j++)
           {
                printf("%5d", ary[i][j]);
           }
           printf("\n");
     }
     return 0;

    /*self 답
    int ary[5][6]={0};
    int i, j, num = 1;
    for (i= 0; i < 4; i++){
        for(j = 0; j < 5; j++){
            ary[i][j] = num;
            num++;            
        }
    }
    for(i = 0;i < 4; i ++){
        ary[i][5] = ary[i][0]+ary[i][1]+ary[i][2]+ary[i][3]+ary[i][4];
    }
    for(j = 0; j < 6; j ++){
        ary[4][j] = ary[0][j]+ary[1][j]+ary[2][j]+ary[3][j];
    }
    for(i= 0; i < 5; i ++){
        for(j = 0; j < 6; j ++){
            printf("%5d", ary[i][j]);
        }
        printf("\n");
    }
    return 0;
    */
}