#include <stdio.h>
#include <unistd.h>

int main(){
    printf("hello, os\n");
    printf("my pid is %d", getpid());

    if (fork() == 0){
        printf("child pid is %d\n", getpid());
    }
    return 0;
}