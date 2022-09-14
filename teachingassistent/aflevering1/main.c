#include <stdio.h>

int main() {
    int input;
    int uger, dage, timer, minutter, sekunder, rest;

    scanf("%d",&input);

    uger = input / 604800;
    rest = input % 604800;
    dage = rest / 86400;
    rest = rest % 86400;
    timer = rest / 3600;
    rest = rest % 3600;
    minutter = rest / 60;
    rest = rest % 60;
    sekunder = rest;

    printf("%d sekunder svarer til: %d uge/r, %d dage, %d timer, %d minutter, %d sekunder\n",input,uger,dage,timer,minutter,sekunder);
    return 0;
}
